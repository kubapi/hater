from django.db import models

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

    # TODO Add timing multiplayer (exponential) and choose some non-linear function to serve as a good scaler
    points = models.IntegerField()

    photo = models.ImageField(upload_to ='card_image', blank = True)

    # Maximum of 2, swipe left means reject swipe left means accept
    accept_choice = models.ForeignKey('self', default = False, null = True, on_delete=models.SET_NULL, related_name='accept_choices', blank=True)
    reject_chocice = models.ForeignKey('self', default = False, null = True,on_delete=models.SET_NULL, related_name='reject_chocices', blank=True)

    # State represents if should be shown in deck
    state = models.BooleanField(default = False)

    INFORMATIONAL = 'INFO'
    ACTION = 'ACT'
    CARD_TYPES = [
        (INFORMATIONAL, 'Informational'),
        (ACTION, 'Action'),
    ]
    card_type = models.CharField(
        max_length = 10,
        choices = CARD_TYPES,
        default = INFORMATIONAL,
    )

    def __str__(self):
        return self.text

class User(models.Model):
    nickname = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    score = models.IntegerField()

    # Add decks finished

    def __str__(self):
        return self.nickname