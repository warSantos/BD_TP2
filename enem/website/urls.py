from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('numberbyage', views.dataNumberByAgeView, name='dataNumberByAgeView'),
    path('numberbygenre', views.dataNumberByGenreView, name='dataNumberByGenreView'),
    path('performancebygenre', views.dataPerformanceByGenreView, name='dataPerformanceByGenreView')
]