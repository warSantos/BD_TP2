from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),    
    path('numberbygenre', views.dataNumberByGenreView, name='dataNumberByGenreView'),
    path('numberbyage', views.dataNumberByAgeView, name='dataNumberByAgeView'),
    path('numberbylanguage', views.dataNumberByLanguageView, name='dataNumberByLanguageView'),
    path('numberbyinternet', views.dataNumberByInternetView, name='dataNumberByInternetView'),
    path('numberbypresence', views.dataNumberByPresenceView, name='dataNumberByPresenceView'),
    path('performancebygenre', views.dataPerformanceByGenreView, name='dataPerformanceByGenreView'),
    path('performancebyestados',views.dataperformanceByEstadosView, name='dataPerformanceByEstadosView')
]