from django.views import generic

from enem.models import Participant

class IndexView(generic.ListView):
    template_name = 'website/content.html'
    context_object_name = 'participants'

    def get_queryset(self):
        query_objects = Participant.objects.all()        
        participants = []
        participants.append({"age": "0-9", "m_value": 0, "f_value": 0})
        participants.append({"age": "10-19", "m_value": 0, "f_value": 0})
        participants.append({"age": "20-29", "m_value": 0, "f_value": 0})
        participants.append({"age": "30-39", "m_value": 0, "f_value": 0})
        participants.append({"age": "40-49", "m_value": 0, "f_value": 0})
        participants.append({"age": "50-59", "m_value": 0, "f_value": 0})
        participants.append({"age": "60-69", "m_value": 0, "f_value": 0})
        participants.append({"age": "70-79", "m_value": 0, "f_value": 0})
        participants.append({"age": "80-99", "m_value": 0, "f_value": 0})
        participants.append({"age": "100+", "m_value": 0, "f_value": 0})
        if (query_objects.count() > 0):
            for participant in query_objects:
                if (participant.genre == "Masculino"):
                    participants[divmod(participant.age, 10)[0]]["m_value"] += 1
                else:
                    participants[divmod(participant.age, 10)[0]]["f_value"] += 1
            for participant in participants:
                participant["m_value"] = (participant["m_value"] / query_objects.count()) * -100
                participant["f_value"] = (participant["f_value"] / query_objects.count()) * 100
        return participants