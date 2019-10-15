from django.shortcuts import render
from .models import Movies
from django.shortcuts import render, redirect
#from . import forms
from django.utils.safestring import mark_safe
import json
from django.contrib.auth.decorators import login_required


def movie_list(request):
    movie = Movies.objects.filter(movie_id=1)
    return render(request, 'movies/movies_list.html', {'movies':movie})
    if request.method == "POST":
        your_name = request.POST["your_name"]
        movie = Movies.objects.filter(movie_id=1)
        return render(request, 'movies/movies_list.html', {'movies':movie, 'your_name': your_name})
    else:
        movie = Movies.objects.filter(movie_id=1)
        return render(request, 'movies/movies_list.html', {'movies':movie})

def index(request):
    return render(request, 'movies/index.html')

movies_categories = [
    {'movie_type': 'Horror', 'genres_to_be_excluded': []},
    {'movie_type': 'Mystery', 'genres_to_be_excluded': ['Horror']},
    {'movie_type': 'Romance', 'genres_to_be_excluded': ['Horror, Mystery']},
    {'movie_type': 'Adventure', 'genres_to_be_excluded': ['Horror, Mystery', 'Romance']},
    {'movie_type': 'Western', 'genres_to_be_excluded': ['Horror, Mystery', 'Romance', 'Adventure']},
    {'movie_type': 'Crime', 'genres_to_be_excluded': ['Horror, Mystery', 'Romance', 'Adventure', 'Western']},
    {'movie_type': 'Science Fiction', 'genres_to_be_excluded': ['Horror, Mystery', 'Romance', 'Adventure', 'Western', 'Crime']},
    {'movie_type': 'Fantasy', 'genres_to_be_excluded': ['Horror, Mystery', 'Romance', 'Adventure', 'Western', 'Crime', 'Sci-Fi']},
    {'movie_type': 'Comedy', 'genres_to_be_excluded': ['Horror, Mystery', 'Romance', 'Adventure', 'Western', 'Crime', 'Sci-Fi', 'Fantasy']},
    {'movie_type': 'Family', 'genres_to_be_excluded': ['Horror, Mystery', 'Romance', 'Adventure', 'Western', 'Crime', 'Sci-Fi', 'Fantasy', 'Comedy']},
    {'movie_type': 'History', 'genres_to_be_excluded': ['Horror, Mystery', 'Romance', 'Adventure', 'Western', 'Crime', 'Sci-Fi', 'Fantasy', 'Comedy', 'Family']},
    {'movie_type': 'War', 'genres_to_be_excluded': ['Horror, Mystery', 'Romance', 'Adventure', 'Western', 'Crime', 'Sci-Fi', 'Fantasy', 'Comedy', 'Family', 'History']},
    {'movie_type': 'Drama', 'genres_to_be_excluded': ['Horror, Mystery', 'Romance', 'Adventure', 'Western', 'Crime', 'Sci-Fi', 'Fantasy', 'Comedy', 'Family', 'History', 'War']},

]

def collect_ratings(request):
    # TODO: implement collecting the ratings

    # render new page with movies to be rated
    request.session['movies_category_index'] = int(request.session.get('movies_category_index',0)) + 1
    if int(request.session['movies_category_index']) == len(movies_categories):
        return render(request, 'movies/bye.html')
    else:
        movie_category = movies_categories[request.session['movies_category_index']]
        movie_type = movie_category['movie_type']
        genres_to_be_excluded = movie_category['genres_to_be_excluded']
        movies = Movies.get_movies_by_genre(movie_type, genres_to_be_excluded )
        return render(request, 'movies/movies_category.html',
            {'movies': movies, 'category': movie_type})

# first page with ratings
def first_movies_category(request):
    request.session['movies_category_index'] = 0

    movie_category = movies_categories[request.session['movies_category_index']]
    movie_type = movie_category['movie_type']
    genres_to_be_excluded = movie_category['genres_to_be_excluded']
    movies = Movies.get_movies_by_genre(movie_type, genres_to_be_excluded )
    return render(request, 'movies/movies_category.html',
        {'movies': movies, 'category': movie_type})
