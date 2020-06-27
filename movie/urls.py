# from django.conf.urls import url
from django.urls import path
from . import views
 
urlpatterns = [
    path('/list', views.MovieList.as_view()),
    path('/add', views.MovieAdd.as_view()),
    path('/<int:pk>', views.MovieDetail.as_view()),
]

