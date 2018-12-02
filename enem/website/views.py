from django.views import generic
from django.db.models import Count, Sum, Avg
from django.shortcuts import render
from django_ajax.decorators import ajax

from enem.models import Participant

@ajax
def dataNumberByGenreView(request):
    query_objects = Participant.objects.values('TP_SEXO').annotate(COUNT = Count('TP_SEXO')).order_by('TP_SEXO')
    data = {
      'result': query_objects
    }
    return data

@ajax
def dataNumberByAgeView(request):
    query_objects = Participant.objects.values('NU_IDADE').annotate(COUNT = Count('NU_IDADE')).order_by('NU_IDADE')
    participants = []
    participants.append({"age": "0-9", "count": 0})
    participants.append({"age": "10-19", "count": 0})
    participants.append({"age": "20-29", "count": 0})
    participants.append({"age": "30-39", "count": 0})
    participants.append({"age": "40-49", "count": 0})
    participants.append({"age": "50-59", "count": 0})
    participants.append({"age": "60-69", "count": 0})
    participants.append({"age": "70-79", "count": 0})
    participants.append({"age": "80-89", "count": 0})
    participants.append({"age": "90-99", "count": 0})
    participants.append({"age": "100+", "count": 0})
    for obj in query_objects:
        if(obj["COUNT"] > 0):
            participants[divmod(int(obj['NU_IDADE']), 10)[0]]["count"] += obj["COUNT"]
    data = {
      'result': participants
    }
    return data

@ajax
def dataNumberByLanguageView(request):
    query_objects = Participant.objects.values('TP_LINGUA').annotate(COUNT = Count('TP_LINGUA'))
    data = {
      'result': query_objects
    }
    return data

@ajax
def dataNumberByInternetView(request):
    query_objects = Participant.objects.values('Q025').annotate(COUNT = Count('Q025'))
    data = {
      'result': query_objects
    }
    return data

@ajax
def dataNumberByPresenceView(request):
    query_objects = {}
    query_objects['DIA1'] = Participant.objects.values('TP_PRESENCA_CH').annotate(COUNT = Count('TP_PRESENCA_CH'))
    query_objects['DIA2'] = Participant.objects.values('TP_PRESENCA_CN').annotate(COUNT = Count('TP_PRESENCA_CN'))
    participants = []
    participants_data = {}
    participants_data['Dia'] = "Dia 1"
    for obj in query_objects['DIA1']:
        if (obj['TP_PRESENCA_CH'] == "0"):
            participants_data['Ausentes'] = obj['COUNT']
        elif (obj['TP_PRESENCA_CH'] == "1"):
            participants_data['Presentes'] = obj['COUNT']
        elif (obj['TP_PRESENCA_CH'] == "2"):
            participants_data['Eliminados'] = obj['COUNT']
    participants.append(participants_data)
    participants_data = {}
    participants_data['Dia'] = "Dia 2"
    for obj in query_objects['DIA2']:
        if (obj['TP_PRESENCA_CN'] == "0"):
            participants_data['Ausentes'] = obj['COUNT']
        elif (obj['TP_PRESENCA_CN'] == "1"):
            participants_data['Presentes'] = obj['COUNT']
        elif (obj['TP_PRESENCA_CN'] == "2"):
            participants_data['Eliminados'] = obj['COUNT']
    participants.append(participants_data)
    data = {
      'result': participants
    }
    return data

@ajax
def dataPerformanceByGenreView(request):
    query_objects = {}
    query_objects['TP_SEXO'] = Participant.objects.values('TP_SEXO').annotate(COUNT = Count('TP_SEXO')).order_by('TP_SEXO')
    query_objects['NU_NOTA'] = Participant.objects.values('TP_SEXO').annotate(
        SUM_NU_NOTA_CN = Sum('NU_NOTA_CN'),
        SUM_NU_NOTA_CH = Sum('NU_NOTA_CH'),
        SUM_NU_NOTA_LC = Sum('NU_NOTA_LC'),
        SUM_NU_NOTA_MT = Sum('NU_NOTA_MT')
    ).order_by('TP_SEXO')
    participants = []
    for obj in query_objects['TP_SEXO']:
        for obj_sum in query_objects['NU_NOTA']:
            if (obj['TP_SEXO'] == obj_sum['TP_SEXO']):
                participants.append({
                    "genre": obj['TP_SEXO'],
                    "media_NOTA_CN": obj_sum['SUM_NU_NOTA_CN'] / obj['COUNT'],
                    "media_NOTA_CH": obj_sum['SUM_NU_NOTA_CH'] / obj['COUNT'],
                    "media_NOTA_LC": obj_sum['SUM_NU_NOTA_LC'] / obj['COUNT'],
                    "media_NOTA_MT": obj_sum['SUM_NU_NOTA_MT'] / obj['COUNT']
                })
                break
    data = {
      'result': participants
    }
    return data


@ajax
def dataperformanceByEstadosView(request):
    query_objects=Participant.objects.values('SG_UF_PROVA').annotate(COUNT=Count('SG_UF_PROVA')).order_by('SG_UF_PROVA')
    query_objects_NU_NOTA = Participant.objects.values('SG_UF_PROVA').annotate(
        SUM_NU_NOTA_CN=Sum('NU_NOTA_CN'),
        SUM_NU_NOTA_CH=Sum('NU_NOTA_CH'),
        SUM_NU_NOTA_LC=Sum('NU_NOTA_LC'),
        SUM_NU_NOTA_MT=Sum('NU_NOTA_MT')

    ).order_by('SG_UF_PROVA')
    participants = []
    for obj in query_objects:
        for obj_sum in query_objects_NU_NOTA:
            if (obj['SG_UF_PROVA'] == obj_sum['SG_UF_PROVA']):
                participants.append({
                    "genre": obj['SG_UF_PROVA'],
                    "media_NOTA_CN": obj_sum['SUM_NU_NOTA_CN'] / obj['COUNT'],
                    "media_NOTA_CH": obj_sum['SUM_NU_NOTA_CH'] / obj['COUNT'],
                    "media_NOTA_LC": obj_sum['SUM_NU_NOTA_LC'] / obj['COUNT'],
                    "media_NOTA_MT": obj_sum['SUM_NU_NOTA_MT'] / obj['COUNT']
                })
                break
    data = {
      'result': participants
    }
    return data


def index(request):
    data = {
      
    }
    return render(request, "website/index.html", data)