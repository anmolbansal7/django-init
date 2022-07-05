from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render
from .models import Movie

# data = {
#     'movies': [
#         {
#             'id': 5,
#             'title': 'Jaws',
#             'year': 1669,
#         },
#         {
#             'id': 6,
#             'title': 'Sharknado',
#             'year': 1660,
#         },
#         {
#             'id': 7,
#             'title': 'The Meg',
#             'year': 1670,
#         }
#     ]
# }


def movies(req):
    data = Movie.objects.all()
    return render(req, 'movies/movies.html', {'movies': data})


def home(req):
    return HttpResponse("Home Page")


def detail(req, id):
    try:
        data = Movie.objects.get(pk=id)
    except:
        raise Http404('Movie does not exist')

    return render(req, 'movies/detail.html', {'movie': data})


def add(req):
    title = req.POST.get('title')
    year = req.POST.get('year')

    if title and year:
        movie = Movie(title=title, year=year)
        movie.save()
        return HttpResponseRedirect('/movies')
    return render(req, 'movies/add.html')


def delete(req, id):
    try:
        movie = Movie.objects.get(pk=id)
    except:
        raise Http404('Movie does not exist')

    movie.delete()
    return HttpResponseRedirect('/movies')
