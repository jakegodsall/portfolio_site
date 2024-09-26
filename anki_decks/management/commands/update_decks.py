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
        if not Path(settings.ANKI_COLLECTION_PATH).is_file():
            self.stdout.write(f"File not found locally. Downloading from S3")
        else:
            self.stdout.write(f"Found local database at: {settings.ANKI_COLLECTION_PATH}")

        # Instantiate the Anki deck exporter
        exporter = AnkiDeckExporter(settings.ANKI_COLLECTION_PATH)

        if len(settings.ANKI_DECKS) == 1 and settings.ANKI_DECKS[0] == '*':
            deck_names = exporter.get_deck_names()  # Process all decks
        else:
            deck_names = settings.ANKI_DECKS  # Process only the decks specified in settings

        # Loop through decks in the collection
        for deck_name in deck_names:
            if deck_name not in exporter.get_deck_names():
                self.stdout.write(f"{deck_name} deck was not found in the database.")
                continue

            new_deck_name = '-'.join(deck_name.split('::'))

            # Export the deck to a temporary file
            export_file_path = exporter.export_deck(deck_name)

            # Check if the deck exists in the database
            existing, created = FlashcardDeck.objects.get_or_create(name=new_deck_name)

            # Open the temporary file and save it to the FileField
            with open(export_file_path, 'rb') as f:
                file_data = File(f)

                output_file = new_deck_name + '.apkg'

                # Save the file, overwriting any existing files with the same name
                if created:
                    existing.deck.save(output_file, file_data)
                else:
                    # Delete the existing file first
                    if existing.deck:
                        existing.deck.delete(save=False)

                    existing.update_upload(output_file, file_data)

            # Clean up the temporary file manually if needed
            os.remove(export_file_path)

            self.stdout.write(f"{new_deck_name} deck has been exported")