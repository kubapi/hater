from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

class Blob(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    text = models.TextField()

    # TODO Add timing multiplayer (exponential) and choose some non-linear function to serve as a good scaler
    points = models.IntegerField()

    photo = models.ImageField(upload_to='blob_images', blank=True)

    # Maximum of 4 choices if blank then is used as a normal text
    first_choice = models.ForeignKey('self')
    second_choice = models.ForeignKey('self', blank=True)
    third_choice = models.ForeignKey('self', blank=True)
    fourth_choice = models.ForeignKey('self', blank=True)

    def __str__(self):
        return self.text

# class Heros(models.Model):
#     name = 
