from django.http import HttpResponse
from django.shortcuts import render

data = {
    'movies': ['The Shawshank Redemption', 'The Godfather', 'The Dark Knight']
}

def movies(request):
    return render(request, 'movies/movies.html', data) # pointing to movies/movies.html template

def home(request):
    return HttpResponse('Home...')