from django.db import models
from django.utils import timezone

class FlashcardDeck(models.Model):
    name = models.CharField(max_length=255)
    link_to_deck = models.URLField(max_length=500)
    initial_upload = models.DateTimeField(auto_now_add=True)
    most_recent_upload = models.DateTimeField(null=True, blank=True)
    number_of_uploads = models.IntegerField(default=0)

    def __str__(self):
        return f"Deck: {self.name}"

    def update_upload(self, new_link):
        self.link_to_deck = new_link
        self.most_recent_upload = timezone.now()
        self.number_of_uploads += 1
        self.save()
