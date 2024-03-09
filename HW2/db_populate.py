import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hw.settings')

django.setup()

from movies.models import Movie
from user.models import User

# Empty row
Movie.objects.all().delete()
User.objects.all().delete()



# Movie instances and For loop
movies = [
    {"movie_name": "Shawshank Redemption", "director": "Frank Darabont", "release_year": 1994, "genre": "Drama", "IMDB_rating": 9.3},
    {"movie_name": "There Will Be Blood", "director": "Paul Thomas Anderson", "release_year": 2007, "genre": "Drama", "IMDB_rating": 8.2},
    {"movie_name": "Gladiator", "director": "Ridley Scott", "release_year": 2000, "genre": "Action", "IMDB_rating": 8.5},
    {"movie_name": "Interstellar", "director": "Christopher Nolan", "release_year": 2014, "genre": "Sci-Fi", "IMDB_rating": 8.6},
    {"movie_name": "Se7en", "director": "David Fincher", "release_year": 1995, "genre": "Crime", "IMDB_rating": 8.6},
    {"movie_name": "Star Wars: Empire Strikes Back", "director": "Irvin Kershner", "release_year": 1980, "genre": "Action", "IMDB_rating": 8.7},
    {"movie_name": "Lord of the Rings: Return of the King", "director": "Peter Jackson", "release_year": 2003, "genre": "Adventure", "IMDB_rating": 8.9},
    {"movie_name": "Dune", "director": "Denis Villeneuve", "release_year": 2021, "genre": "Sci-Fi", "IMDB_rating": 8.6},
    {"movie_name": "Die Hard", "director": "John McTiernan", "release_year": 1988, "genre": "Action", "IMDB_rating": 8.2},
    {"movie_name": "Blade Runner 2049", "director": "Denis Villeneuve", "release_year": 2017, "genre": "Sci-Fi", "IMDB_rating": 8.0},
]

for movie_info in movies:
    movie = Movie(**movie_info)
    movie.save()
  

# Customer instances and for loop
customers = [
    {'userName':'tommyrey152', 'firstName':'Tommy', 'lastName':'Reynolds', 'email':'tommyrey152@gmail.com','birthday':'2001-07-20','fav_genre':'Drama/Action','fav_movie':'Shawshank Redemption'},
    {'userName':'johndoe123', 'firstName':'John', 'lastName':'Doe', 'email':'johndoe123@normal.com','birthday':'2000-01-01','fav_genre':'Horror','fav_movie':'The Shining'},
    {'userName':'jimmyBuffet_margs', 'firstName':'Jimmy', 'lastName':'Buffett', 'email':'parrots@margaritaville.com','birthday':'1936-12-25','fav_genre':'Comedy','fav_movie':'Donovans Reef'}
]

for customer_info in customers:
    cust = User(**customer_info)
    cust.save()




# Django QuerySet



