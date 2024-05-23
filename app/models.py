from django.db import models

# Create your models here.

class Translate(models.Model):
    image = models.ImageField(upload_to='images/')
    french_text = models.TextField()
    english_text = models.TextField()

    def __str__(self):
        return self.french_text