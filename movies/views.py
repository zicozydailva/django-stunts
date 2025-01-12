from django.http import HttpResponse

def movies(request):
    return HttpResponse('Movie...')

def home(request):
    return HttpResponse('Home...')