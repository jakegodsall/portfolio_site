import os
from pathlib import Path

import boto3
from django.core.management.base import BaseCommand
from django.core.files import File
from django.conf import settings

from anki_decks.models import FlashcardDeck
from anki_decks.anki_service import AnkiDeckExporter


class Command(BaseCommand):
    help = "Export anki decks and update the database"

    def download_db_from_s3(s3_bucket, s3_key, download_path):
        s3 = boto3.client('s3')
        s3.download_file(s3_bucket, s3_key, download_path)

    def handle(self, *args, **kwargs):
        # Path for the sqlite anki database
        anki_collection_path = settings.ANKI_COLLECTION_PATH
        # list of deck names to export
        anki_decks = settings.ANKI_DECKS

        print("PATH", anki_collection_path)

        if not Path(anki_collection_path).is_file():
            self.stdout.write(f"File not found locally. Downloading from S3")
        else:
            self.stdout.write(f"Found local database at: {anki_collection_path}")

        # Instantiate the Anki deck exporter
        exporter = AnkiDeckExporter(anki_collection_path)

        if len(anki_decks) == 1 and anki_decks[0] == '*':
            deck_names = exporter.get_deck_names()  # Process all decks
        else:
            deck_names = anki_decks  # Process only the decks specified in settings

        # Loop through decks in the collection
        for deck_name in deck_names:
            deck_name = deck_name.split('::')[-1]
            # Export the decks
            export_file_path = exporter.export_deck(deck_name, '')

            # Check if the deck exists in the database
            existing, created = FlashcardDeck.objects.get_or_create(name=deck_name)

            # Open the exported file and save it to the FileField
            with open(export_file_path, 'rb') as f:
                file_data = File(f)

                # Extract the final part of the deck name after the last '::'
                valid_filename = deck_name.split("::")[-1]

                # Clean the final part for the filename
                valid_filename = valid_filename + '.apkg'

                # Save the file, overwriting any existing files with the same name
                if created:
                    existing.deck.save(valid_filename, file_data)
                else:
                    # Delete the existing file first (if you want to replace it)
                    if existing.deck:
                        existing.deck.delete(save=False)

                    # Overwrite the existing file with the same name
                    existing.deck.save(valid_filename, file_data)
            self.stdout.write(f"{deck_name} deck has been exported")
