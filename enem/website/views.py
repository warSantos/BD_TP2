from django.views import generic
from django.db.models import Count

from enem.models import Participant

class IndexView(generic.ListView):
    template_name = 'website/content.html'
    context_object_name = 'participants'

    def get_queryset(self):
        # query_objects = Participant.objects.all()
        # qo_m = Participant.objects.filter(TP_SEXO = "M").count()
        # qo_m = Participant.objects.values('TP_SEXO')
        # Participant.objects.annotate(Count('TP_SEXO', distinct=True)),
        # qo_m = Participant.objects.aggregate(Participant.objects.annotate(Count('TP_SEXO', distinct=True)), allowDiskUse= True)
        # qo_m = Participant.objects.filter(NU_IDADE = 5).count()
        # for i in range(10):
        #     qo_m1 = qo_m.filter(NU_IDADE = i)
        #     print(qo_m1.count())
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
        for participant in query_objects:
            if(participant["COUNT"] > 0):
                print (participant)
                participants[divmod(int(participant['NU_IDADE']), 10)[0]]["count"] += participant["COUNT"]
        return participants