from pathlib import Path
from anki.storage import Collection
from anki.exporting import AnkiPackageExporter


class AnkiDeckExporter:
    def __init__(self, collection_path):
        # Initialize the Anki collection
        self.collection_path = Path(collection_path)
        self.col = Collection(str(self.collection_path))

    def get_decks_by_prefix(self, prefix):
        # Get all decks and filter by a prefix
        decks = self.col.decks.all()
        filtered_decks = [deck for deck in decks if deck['name'].startswith(prefix)]
        return filtered_decks

    def get_decks_by_array(self, deck_names):
        # Get decks by an array of deck names
        decks = self.col.decks.all()
        filtered_decks = [deck for deck in decks if deck['name'] in deck_names]
        return decks

    def get_deck_names(self, prefix):
        # Get names of all decks
        decks = self.col.decks.all()
        return [deck['name'] for deck in decks]

    def get_deck_names_by_prefix(self, prefix):
        # Get names of decks that match the prefix
        filtered_decks = self.get_decks_by_prefix(prefix)
        deck_names = [deck['name'] for deck in filtered_decks]
        return deck_names



    def get_cards_from_deck(self, deck_id):
        # Get all cards from a specific deck by deck_id
        cards = self.col.db.all(f'SELECT * FROM cards WHERE did={deck_id}')
        return cards

    def export_deck(self, deck_name, export_path='/tmp'):
        # Export a deck by name to a specified path
        deck_id = self.col.decks.id(deck_name)

        # Create an AnkiPackageExporter and set it to export the specific deck
        exporter = AnkiPackageExporter(self.col)

        # Set the deck ID to export the desired deck
        exporter.did = deck_id

        # Exclude scheduling data if desired
        exporter.includeSched = False

        # Set the export file path
        export_file_path = f'{export_path}/{deck_name}.apkg'

        # Perform the export
        exporter.exportInto(export_file_path)

        return export_file_path



