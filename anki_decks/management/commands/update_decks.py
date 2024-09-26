import os
from django.core.management.base import BaseCommand
from django.core.files import File
from django.conf import settings

from anki_decks.models import FlashcardDeck
from anki_decks.anki_service import AnkiDeckExporter


class Command(BaseCommand):
    help = "Export anki decks and update the database"

    def handle(self, *args, **kwargs):
        anki_collection_path = settings.ANKI_COLLECTION_PATH
        anki_decks = settings.ANKI_DECKS

        # Instantiate the Anki deck exporter
        exporter = AnkiDeckExporter(anki_collection_path)

        if len(anki_decks) == 1 and anki_decks[0] == '*':
            deck_names = exporter.get_deck_names()  # Process all decks
        else:
            deck_names = anki_decks  # Process only the decks specified in settings

        # Loop through decks in the collection
        for deck_name in deck_names:
            # Export the decks
            export_file_path = exporter.export_deck(deck_name)

            # Check if the deck exists in the database
            existing, created = FlashcardDeck.objects.get_or_create(name=deck_name)

            # Open the exported file and save it to the FileField
            with open(export_file_path, 'rb') as f:
                file_data = File(f)

                # Update the existing deck or save a new entry
                if created:
                    existing.deck.save(f'{deck_name}.apkg', file_data)
                else:
                    existing.update_upload(file_data)
