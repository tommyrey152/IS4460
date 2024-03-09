from django.db import models


# User Attributes
class User(models.Model):
    userName = models.CharField(max_length = 100)
    firstName = models.CharField(max_length = 100)
    lastName = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 150)
    birthday = models.DateField(null=True, blank=True)
    fav_genre = models.CharField(max_length = 100)
    fav_movie = models.CharField(max_length = 100)

    def __str__(self):
        return self.userName




