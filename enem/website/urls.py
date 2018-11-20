from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('age', views.dataAgeView, name='dataAgeView'),
    path('genre', views.dataGenreView, name='dataGenreView')
    # path('age', views.IndexView.as_view(), name='index')
]