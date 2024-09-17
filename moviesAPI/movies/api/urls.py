# from django.conf.urls import url
# from .views import getMovieFunction


# urlpattern = [
#     url('getMovie', getMovieFunction)
# ]

from . import views
from django.urls import path, re_path

urlpatterns = [
    path('getMovie/', views.getMovieFunction, name='getMovieFunction'),
    path('saveMovie/', views.SaveMovieFunction, name='SaveMovieFunction'),
    path('bulkMovie/', views.BulkMovie, name='BulkMovie')
]