from django.urls import path

from . import views

urlpatterns = [
    path('run/', views.genreClassify,name='genreClassify'),
]