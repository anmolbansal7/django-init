from django.http import HttpResponse
from django.shortcuts import render

data = {
    'movies': [
        {
            'id': 5,
            'title': 'Jaws',
            'year': 1669,
        },
        {
            'id': 6,
            'title': 'Sharknado',
            'year': 1660,
        },
        {
            'id': 7,
            'title': 'The Meg',
            'year': 1670,
        }
    ]
}


def movies(req):
    return render(req, 'movies/movies.html', data)


def home(req):
    return HttpResponse("Home Page")
