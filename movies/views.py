from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie
# data = {
#     'movies': [{'id': 1, 'title': 'The Shawshank Redemption', 'year': 1994}, {'id:': 2, 'title': 'The Godfather', 'year': 1972}, {'id': 3, 'title': 'The Dark Knight', 'year': 2008}, {'id:': 4, 'title': 'The Lord of the Rings: The Return of the King', 'year': 2003}, {'id': 5, 'title': 'Pulp Fiction', 'year': 1994}]
# }

def movies(request):
    data = Movie.objects.all() # to fetch all movies from DB
    return render(request, 'movies/movies.html', {'movies': data}) # pointing to movies/movies.html template

def home(request):
    return HttpResponse('Home...')