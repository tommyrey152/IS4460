from django.db import models


# Movie Attributes
class Movie(models.Model):
    movie_name = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    release_year = models.IntegerField(null=True, blank=True)
    genre = models.CharField(max_length=50)
    IMDB_rating = models.FloatField()
     



