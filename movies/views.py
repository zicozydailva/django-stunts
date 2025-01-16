from django.http import HttpResponse, HttpResponseRedirect
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

def detail(request, id):
    data = Movie.objects.get(pk=id)
    return render(request, 'movies/detail.html', {'movie': data})

def add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        year = request.POST.get('year')
        if title and year:
         movie = Movie(title=title, year=year)
         movie.save()
         return HttpResponseRedirect('/movies')
    return render(request, 'movies/add.html')

def delete(request, id):
    movie = Movie.objects.get(pk=id)
    movie.delete()
    return HttpResponseRedirect('/movies')