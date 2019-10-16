from django.conf.urls import url

from . import views

app_name = 'movie'

urlpatterns = [
    url(r'^test_rating/$', views.test_rating, name='test_rating'),
    url(r'^collect_ratings/$', views.collect_ratings, name='collect_ratings'),
    url(r'^first_movies_category/$', views.first_movies_category, name='first_movies_category'),
    url(r'^insert_rating/$', views.insert_rating, name='insert_rating'),
]
