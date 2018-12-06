from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('info', views.info, name='info'),
    path('numberbygenre', views.dataNumberByGenreView, name='dataNumberByGenreView'),
    path('numberbyage', views.dataNumberByAgeView, name='dataNumberByAgeView'),
    path('numberbyschool', views.dataNumberBySchoolView, name='dataNumberBySchoolView'),
    path('numberbylanguage', views.dataNumberByLanguageView, name='dataNumberByLanguageView'),
    path('numberbyinternet', views.dataNumberByInternetView, name='dataNumberByInternetView'),
    path('numberbypresence', views.dataNumberByPresenceView, name='dataNumberByPresenceView'),
    path('numberbyincome',views.dataNumberByIncomeView, name='dataNumberByIncomeView'),
    path('performancebygenre', views.dataPerformanceByGenreView, name='dataPerformanceByGenreView'),
    path('performancebyschool', views.dataPerformanceBySchoolView, name='dataPerformanceBySchoolView'),
    path('performancebyestados', views.dataperformanceByEstadosView, name='dataPerformanceByEstadosView'),
    path('situacaoensinomedio', views.dataSituacaoEnsinoMedioView, name='dataSituacaoEnsinoMedioView'),
    path('performancebyetinico', views.dataperformanceByEtinicoView, name='dataperformanceByEtinicoView'),
    path('performancebyincome', views.dataPerformanceByIncomeView, name='dataPerformanceByIncomeView'),
    path('performancebyinternet', views.dataPerformanceByInternetView, name='dataPerformanceByInternetView'),
    path('cornumero',views.datacornumeroView,name='datacornumeroView')
]