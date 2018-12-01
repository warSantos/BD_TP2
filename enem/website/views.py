from django.views import generic
from django.db.models import Count, Sum, Avg
from django.shortcuts import render
from django_ajax.decorators import ajax

from enem.models import Participant

@ajax
def dataNumberByAgeView(request):
    query_objects = Participant.objects.values('NU_IDADE').annotate(COUNT=Count('NU_IDADE')).order_by('NU_IDADE')
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
def dataNumberByGenreView(request):
    query_objects = Participant.objects.values('TP_SEXO').annotate(COUNT=Count('TP_SEXO')).order_by('TP_SEXO')
    data = {
      'result': query_objects
    }
    return data

@ajax
def dataPerformanceByGenreView(request):
    query_objects = Participant.objects.values('TP_SEXO').annotate(COUNT=Count('TP_SEXO')).order_by('TP_SEXO')
    query_objects_NU_NOTA = Participant.objects.values('TP_SEXO').annotate(
        SUM_NU_NOTA_CN=Sum('NU_NOTA_CN'),
        SUM_NU_NOTA_CH=Sum('NU_NOTA_CH'),
        SUM_NU_NOTA_LC=Sum('NU_NOTA_LC'),
        SUM_NU_NOTA_MT=Sum('NU_NOTA_MT')
    ).order_by('TP_SEXO')
    print(query_objects )
    print(query_objects_NU_NOTA)
    participants = []
    for obj in query_objects:
        for obj_sum in query_objects_NU_NOTA:
            if (obj['TP_SEXO'] == obj_sum['TP_SEXO']):
                participants.append({
                    "genre": obj['TP_SEXO'],
                    "media_NOTA_CN": obj_sum['SUM_NU_NOTA_CN'] / obj['COUNT'],
                    "media_NOTA_CH": obj_sum['SUM_NU_NOTA_CH'] / obj['COUNT'],
                    "media_NOTA_LC": obj_sum['SUM_NU_NOTA_LC'] / obj['COUNT'],
                    "media_NOTA_MT": obj_sum['SUM_NU_NOTA_MT'] / obj['COUNT']
                })
                break
    print(participants)
    data = {
      'result': participants
    }
    return data

def index(request):
    data = {
      
    }
    return render(request, "website/index.html", data)


# class DataAgeView(generic.ListView):
#     template_name = 'website/content.html'
#     context_object_name = 'participants'

#     def get_queryset(self):
#         # query_objects = Participant.objects.all()
#         # qo_m = Participant.objects.filter(TP_SEXO = "M").count()
#         # qo_m = Participant.objects.values('TP_SEXO')
#         # Participant.objects.annotate(Count('TP_SEXO', distinct=True)),
#         # qo_m = Participant.objects.aggregate(Participant.objects.annotate(Count('TP_SEXO', distinct=True)), allowDiskUse= True)
#         # qo_m = Participant.objects.filter(NU_IDADE = 5).count()
#         # for i in range(10):
#         #     qo_m1 = qo_m.filter(NU_IDADE = i)
#         #     print(qo_m1.count())
#         query_objects = Participant.objects.values('NU_IDADE').annotate(COUNT=Count('NU_IDADE')).order_by('NU_IDADE')
#         participants = []
#         participants.append({"age": "0-9", "count": 0})
#         participants.append({"age": "10-19", "count": 0})
#         participants.append({"age": "20-29", "count": 0})
#         participants.append({"age": "30-39", "count": 0})
#         participants.append({"age": "40-49", "count": 0})
#         participants.append({"age": "50-59", "count": 0})
#         participants.append({"age": "60-69", "count": 0})
#         participants.append({"age": "70-79", "count": 0})
#         participants.append({"age": "80-89", "count": 0})
#         participants.append({"age": "90-99", "count": 0})
#         participants.append({"age": "100+", "count": 0})
#         for participant in query_objects:
#             if(participant["COUNT"] > 0):
#                 print (participant)
#                 participants[divmod(int(participant['NU_IDADE']), 10)[0]]["count"] += participant["COUNT"]
#         return participants

# class IndexView(generic.ListView):
#     template_name = 'website/content.html'
#     context_object_name = 'participants'