from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Deck(models.Model):
    deck_name = models.CharField(max_length=100)

    def __str__(self):
        return self.deck_name

    def get_cards(self):
        return self.card_set.all()

    class Meta:
        verbose_name_plural = "Decks"

class Card(models.Model):
    deck = models.ForeignKey(Deck, on_delete = models.CASCADE)
    text = models.TextField()
    title = models.CharField(default="Tytuł X", max_length=100)

    points = models.IntegerField()

    image = models.ImageField(upload_to ='card_image', blank = True)

    accept_choice_info = models.CharField(max_length=255, default="Tak")
    reject_choice_info = models.CharField(max_length=255, default="Nie")

    # Maximum of 2, swipe left means reject swipe left means accept
    accept_choice = models.ForeignKey('self', default = False, null = True, on_delete=models.SET_NULL, related_name='accept_choices', blank=True)
    reject_choice = models.ForeignKey('self', default = False, null = True,on_delete=models.SET_NULL, related_name='reject_chocices', blank=True)

    # State represents if should be shown in deck
    is_active = models.BooleanField(default = False)

    INFORMATIONAL = 'INFO'
    ACTION = 'ACT'
    CATEGORIES = [
        (INFORMATIONAL, 'Informational'),
        (ACTION, 'Action'),
    ]
    category = models.CharField(
        max_length = 10,
        choices = CATEGORIES,
        default = INFORMATIONAL,
    )

    def __str__(self):
        return self.text

# Extending on existing User model from Auth
class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.IntegerField(default = 0)

    architect = models.BooleanField(default = False)
    # finished_decks = models.ForeignKey(Deck, on_delete=models.PROTECT)

    def __str__(self):
        return self.user.username