from django.db import models


# Create your models here.
class Show(models.Model):
    name = models.CharField(("Name of the show"), max_length=50)
    fav = models.CharField(("Favourite Character"), max_length=50)

    def __str__(self):
        return self.name
