from django.views import generic
from django.db.models import Count, Sum, Avg
from django.shortcuts import render
from django_ajax.decorators import ajax

from enem.models import Participant
from django.views.decorators.csrf import csrf_exempt

@ajax
@csrf_exempt
def dataNumberByGenreView(request):
    if (request.method == 'POST'):
        place = request.POST.get('place')
        if (place != "BR"):
            query_objects = Participant.objects.filter(SG_UF_PROVA=place).values('TP_SEXO').annotate(COUNT = Count('TP_SEXO')).order_by('TP_SEXO')
        else:
            query_objects = Participant.objects.values('TP_SEXO').annotate(COUNT = Count('TP_SEXO')).order_by('TP_SEXO')
        data = {
            'result': query_objects
        }
        return data

@ajax
@csrf_exempt
def dataNumberByAgeView(request):
    if (request.method == 'POST'):
        place = request.POST.get('place')
        if (place != "BR"):
            query_objects = Participant.objects.filter(SG_UF_PROVA=place).values('NU_IDADE').annotate(COUNT = Count('NU_IDADE')).order_by('NU_IDADE')
        else:
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
@csrf_exempt
def dataNumberBySchoolView(request):
    if (request.method == 'POST'):
        titles = {
            '1': "Não Respondeu",
            '2': "Pública",
            '3': "Privada",
            '4': "Exterior"
        }
        place = request.POST.get('place')
        if (place != "BR"):
            query_objects = Participant.objects.filter(SG_UF_PROVA=place).values('TP_ESCOLA').annotate(COUNT = Count('TP_ESCOLA')).order_by('TP_ESCOLA')
        else:
            query_objects = Participant.objects.values('TP_ESCOLA').annotate(COUNT = Count('TP_ESCOLA')).order_by('TP_ESCOLA')
        result = []
        for obj in query_objects:
            result.append({"title": titles[obj["TP_ESCOLA"]], "value": obj['COUNT']})
        data = {
            'result': result
        }
        return data

@ajax
@csrf_exempt
def dataNumberByLanguageView(request):
    if (request.method == 'POST'):
        place = request.POST.get('place')
        if(place !="BR"):
            query_objects = Participant.objects.filter(SG_UF_PROVA=place).values('TP_LINGUA').annotate(COUNT = Count('TP_LINGUA'))
        else:
            query_objects = Participant.objects.values('TP_LINGUA').annotate(COUNT = Count('TP_LINGUA'))
        data = {
            'result': query_objects
        }
        return data

@ajax
@csrf_exempt
def dataNumberByInternetView(request):
    if (request.method == 'POST'):
        place = request.POST.get('place')
        if(place != "BR"):
            query_objects = Participant.objects.filter(SG_UF_PROVA=place).values('Q025').annotate(COUNT = Count('Q025'))
        else:
            query_objects = Participant.objects.values('Q025').annotate(COUNT = Count('Q025'))
        data = {
            'result': query_objects
        }
        return data

@ajax
@csrf_exempt
def dataNumberByPresenceView(request):
    if (request.method == 'POST'):
        titles = {
            '0': "Ausentes",
            '1': "Presentes",
            '2': "Eliminados"
        }
        query_objects = {}
        place = request.POST.get('place')
        if(place != "BR"):
            query_objects['DIA1'] = Participant.objects.filter(SG_UF_PROVA=place).values('TP_PRESENCA_CH').annotate(COUNT = Count('TP_PRESENCA_CH'))
            query_objects['DIA2'] = Participant.objects.filter(SG_UF_PROVA=place).values('TP_PRESENCA_CN').annotate(COUNT = Count('TP_PRESENCA_CN'))
        else:
            query_objects['DIA1'] = Participant.objects.values('TP_PRESENCA_CH').annotate(COUNT = Count('TP_PRESENCA_CH'))
            query_objects['DIA2'] = Participant.objects.values('TP_PRESENCA_CN').annotate(COUNT = Count('TP_PRESENCA_CN'))
        participants = []
        participants_data = {}
        participants_data['Dia'] = "Dia 1"
        for obj in query_objects['DIA1']:
            if (obj['TP_PRESENCA_CH'] != ""):
                participants_data[titles[obj["TP_PRESENCA_CH"]]] = obj['COUNT']
        participants.append(participants_data)
        participants_data = {}
        participants_data['Dia'] = "Dia 2"
        for obj in query_objects['DIA2']:
            if (obj['TP_PRESENCA_CN'] != ""):
                participants_data[titles[obj["TP_PRESENCA_CN"]]] = obj['COUNT']
        participants.append(participants_data)
        data = {
            'result': participants
        }
        return data

@ajax
@csrf_exempt
def dataNumberByIncomeView(request):
    titles={
        'A': 'Nenhuma renda.',
        'B': 'Até R$ 937,00.',
        'C': 'De R$ 937,01 até R$ 1.405,50.',
        'D': 'De R$ 1.405,51 até R$ 1.874,00.',
        'E': 'De R$ 1.874,01 até R$ 2.342,50.',
        'F': 'De R$ 2.342,51 até R$ 2.811,00.',
        'G': 'De R$ 2.811,01 até R$ 3.748,00.',
        'H': 'De R$ 3.748,01 até R$ 4.685,00.',
        'I': 'De R$ 4.685,01 até R$ 5.622,00.',
        'J': 'De R$ 5.622,01 até R$ 6.559,00.',
        'K': 'De R$ 6.559,01 até R$ 7.496,00.',
        'L': 'De R$ 7.496,01 até R$ 8.433,00.',
        'M': 'De R$ 8.433,01 até R$ 9.370,00.',
        'N': 'De R$ 9.370,01 até R$ 11.244,00.',
        'O': 'De R$ 11.244,01 até R$ 14.055,00.',
        'P': 'De R$ 14.055,01 até R$ 18.740,00.',
        'Q': 'Mais de R$ 18.740,00.'
    }

    if(request.method== 'POST'):
        place= request.POST.get('place')
        data = []
        query_entry = []
        if(place != "BR"):
            query_entry = Participant.objects.filter(SG_UF_PROVA=place).values("Q006","TP_SEXO").\
                    annotate(entries=Count("Q006","TP_SEXO"))
        else:
            query_entry = Participant.objects.values("Q006","TP_SEXO").\
                    annotate(entries=Count("Q006","TP_SEXO"))
                    
        for i in titles:
            elem_class = [x for x in query_entry if x["Q006"] == i]
            masc = [x for x in elem_class if x['TP_SEXO'] == 'M']
            femi = [x for x in elem_class if x['TP_SEXO'] == 'F']
                 
            data.append({
                'Classe': titles[i], 
                'Masculino': 0 if not masc else masc[0]['entries'],
                'Feminino': 0 if not femi else femi[0]['entries']
            })

        return data

@ajax
@csrf_exempt
def dataPerformanceByGenreView(request):
    if(request.method == 'POST'):
        place = request.POST.get('place')
        query_objects = {}
        if(place != "BR"):
            query_objects['TP_SEXO'] = Participant.objects.filter(SG_UF_PROVA=place).values('TP_SEXO').annotate(COUNT = Count('TP_SEXO')).order_by('TP_SEXO')
            query_objects['NU_NOTA'] = Participant.objects.filter(SG_UF_PROVA=place).values('TP_SEXO').annotate(
                SUM_NU_NOTA_CN = Sum('NU_NOTA_CN'),
                SUM_NU_NOTA_CH = Sum('NU_NOTA_CH'),
                SUM_NU_NOTA_LC = Sum('NU_NOTA_LC'),
                SUM_NU_NOTA_MT = Sum('NU_NOTA_MT'),
                SUM_NU_NOTA_REDACAO = Sum('NU_NOTA_REDACAO')
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
                            "media_NOTA_MT": obj_sum['SUM_NU_NOTA_MT'] / obj['COUNT'],
                            "media_NOTA_REDACAO": obj_sum['SUM_NU_NOTA_REDACAO'] / obj['COUNT']
                        })
                        break

        else:
            query_objects['TP_SEXO'] = Participant.objects.values('TP_SEXO').annotate(COUNT = Count('TP_SEXO')).order_by('TP_SEXO')
            query_objects['NU_NOTA'] = Participant.objects.values('TP_SEXO').annotate(
                SUM_NU_NOTA_CN = Sum('NU_NOTA_CN'),
                SUM_NU_NOTA_CH = Sum('NU_NOTA_CH'),
                SUM_NU_NOTA_LC = Sum('NU_NOTA_LC'),
                SUM_NU_NOTA_MT = Sum('NU_NOTA_MT'),
                SUM_NU_NOTA_REDACAO = Sum('NU_NOTA_REDACAO')
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
                            "media_NOTA_MT": obj_sum['SUM_NU_NOTA_MT'] / obj['COUNT'],
                            "media_NOTA_REDACAO": obj_sum['SUM_NU_NOTA_REDACAO'] / obj['COUNT']
                        })
                        break
        data = {
        'result': participants
        }
        return data

@ajax
@csrf_exempt
def dataPerformanceBySchoolView(request):
    if (request.method == 'POST'):
        titles = {
            '1': "Não Respondeu",
            '2': "Pública",
            '3': "Privada",
            '4': "Exterior"
        }
        place = request.POST.get('place')
        query_objects = {}
        if (place != "BR"):
            query_objects['TP_ESCOLA'] = Participant.objects.filter(SG_UF_PROVA=place).values('TP_ESCOLA').annotate(COUNT = Count('TP_ESCOLA')).order_by('TP_ESCOLA')
            query_objects['NU_NOTA'] = Participant.objects.filter(SG_UF_PROVA=place).values('TP_ESCOLA').annotate(
                SUM_NU_NOTA_CN = Sum('NU_NOTA_CN'),
                SUM_NU_NOTA_CH = Sum('NU_NOTA_CH'),
                SUM_NU_NOTA_LC = Sum('NU_NOTA_LC'),
                SUM_NU_NOTA_MT = Sum('NU_NOTA_MT'),
                SUM_NU_NOTA_REDACAO = Sum('NU_NOTA_REDACAO')
            ).order_by('TP_ESCOLA')
        else:
            query_objects['TP_ESCOLA'] = Participant.objects.values('TP_ESCOLA').annotate(COUNT = Count('TP_ESCOLA')).order_by('TP_ESCOLA')
            query_objects['NU_NOTA'] = Participant.objects.values('TP_ESCOLA').annotate(
                SUM_NU_NOTA_CN = Sum('NU_NOTA_CN'),
                SUM_NU_NOTA_CH = Sum('NU_NOTA_CH'),
                SUM_NU_NOTA_LC = Sum('NU_NOTA_LC'),
                SUM_NU_NOTA_MT = Sum('NU_NOTA_MT'),
                SUM_NU_NOTA_REDACAO = Sum('NU_NOTA_REDACAO')
            ).order_by('TP_ESCOLA')
        participants = []
        for obj in query_objects['TP_ESCOLA']:
            for obj_sum in query_objects['NU_NOTA']:
                if (obj['TP_ESCOLA'] == obj_sum['TP_ESCOLA']):
                    participants.append({
                        "escola": titles[obj["TP_ESCOLA"]],
                        "media": round(((obj_sum['SUM_NU_NOTA_CN'] / obj['COUNT']) + (obj_sum['SUM_NU_NOTA_CH'] / obj['COUNT']) + (obj_sum['SUM_NU_NOTA_LC'] / obj['COUNT']) + (obj_sum['SUM_NU_NOTA_MT'] / obj['COUNT']) + (obj_sum['SUM_NU_NOTA_REDACAO'] / obj['COUNT'])) / 5, 2)
                    })
                    break
        data = {
            'result': participants
        }
        return data

@ajax
@csrf_exempt
def dataperformanceByEstadosView(request):
    if (request.method == 'POST'):
        place = request.POST.get('place')
        query_objects = {}
        participants = []
        if (place != "BR"):
            query_objects['SG_UF_PROVA'] = Participant.objects.filter(SG_UF_PROVA=place).values('SG_UF_PROVA').annotate(COUNT = Count('SG_UF_PROVA')).order_by('SG_UF_PROVA')
            query_objects['NU_NOTA'] = Participant.objects.filter(SG_UF_PROVA=place).values('SG_UF_PROVA').annotate(
                SUM_NU_NOTA_CN = Sum('NU_NOTA_CN'),
                SUM_NU_NOTA_CH = Sum('NU_NOTA_CH'),
                SUM_NU_NOTA_LC = Sum('NU_NOTA_LC'),
                SUM_NU_NOTA_MT = Sum('NU_NOTA_MT'),
                SUM_NU_NOTA_REDACAO = Sum('NU_NOTA_REDACAO')
            ).order_by('SG_UF_PROVA')
            for obj in query_objects['SG_UF_PROVA']:
                for obj_sum in query_objects['NU_NOTA']:
                    if (obj['SG_UF_PROVA'] == obj_sum['SG_UF_PROVA']):
                        participants.append({"title": "Ciências Humanas", "value": obj_sum['SUM_NU_NOTA_CH'] / obj['COUNT']})
                        participants.append({"title": "Ciências da Natureza", "value": obj_sum['SUM_NU_NOTA_CN'] / obj['COUNT']})
                        participants.append({"title": "Linguagens e Códigos", "value": obj_sum['SUM_NU_NOTA_LC'] / obj['COUNT']})
                        participants.append({"title": "Matemática", "value": obj_sum['SUM_NU_NOTA_MT'] / obj['COUNT']})
                        participants.append({"title": "Redação", "value": obj_sum['SUM_NU_NOTA_REDACAO'] / obj['COUNT']})
                        break
        else:
            query_objects['SG_UF_PROVA'] = Participant.objects.values('SG_UF_PROVA').annotate(COUNT = Count('SG_UF_PROVA')).order_by('SG_UF_PROVA')
            query_objects['NU_NOTA'] = Participant.objects.values('SG_UF_PROVA').annotate(
                SUM_NU_NOTA_CN = Sum('NU_NOTA_CN'),
                SUM_NU_NOTA_CH = Sum('NU_NOTA_CH'),
                SUM_NU_NOTA_LC = Sum('NU_NOTA_LC'),
                SUM_NU_NOTA_MT = Sum('NU_NOTA_MT'),
                SUM_NU_NOTA_REDACAO = Sum('NU_NOTA_REDACAO')
            ).order_by('SG_UF_PROVA')
            for obj in query_objects['SG_UF_PROVA']:
                for obj_sum in query_objects['NU_NOTA']:
                    if (obj['SG_UF_PROVA'] == obj_sum['SG_UF_PROVA']):
                        participants.append({
                            "estado": obj['SG_UF_PROVA'],
                            "media": round(((obj_sum['SUM_NU_NOTA_CN'] / obj['COUNT']) + (obj_sum['SUM_NU_NOTA_CH'] / obj['COUNT']) + (obj_sum['SUM_NU_NOTA_LC'] / obj['COUNT']) + (obj_sum['SUM_NU_NOTA_MT'] / obj['COUNT']) + (obj_sum['SUM_NU_NOTA_REDACAO'] / obj['COUNT'])) / 5, 2)
                        })
                        break
        data = {
            'result': participants
        }
        return data

@ajax
@csrf_exempt
def dataSituacaoEnsinoMedioView(request):
    if (request.method == 'POST'):
        titles = {
            '1': "Já concluí",
            '2': "Estou cursando e concluirei em 2017",
            '3': "Estou cursando e concluirei após 2017",
            '4': "Não concluí e não estou cursando"
        }
        place= request.POST.get('place')
        if(place != "BR"):
            query_entry = Participant.objects.filter(SG_UF_PROVA=place).values("TP_ST_CONCLUSAO").annotate(entries=Count("TP_ST_CONCLUSAO"))
            data = []
            for i in query_entry:
                data.append({"title": titles[i["TP_ST_CONCLUSAO"]], "value": i['entries']})

        else:            
            query_entry = Participant.objects.values("TP_ST_CONCLUSAO").annotate(entries=Count("TP_ST_CONCLUSAO"))
            data = []
            for i in query_entry:
                data.append({"title": titles[i["TP_ST_CONCLUSAO"]], "value": i['entries']})

        # print(data)
        return data
@ajax
@csrf_exempt
def dataperformanceByEtinicoView(request):
    if (request.method == 'POST'):
        titles = {
            '0': "Nao_declarado",
            '1': "Branca",
            '2': "Preta",
            '3': "Parda",
            '4': "Amarela",
            '5': "Indigena"
        }
        place = request.POST.get('place')
        query_objects = {}
        if(place != "BR"):
            query_objects['TP_COR_RACA'] = Participant.objects.filter(SG_UF_PROVA=place).values('TP_COR_RACA').annotate(COUNT = Count('TP_COR_RACA')).order_by('TP_COR_RACA')
            query_objects['NU_NOTA'] = Participant.objects.filter(SG_UF_PROVA=place).values('TP_COR_RACA').annotate(
                SUM_NU_NOTA_CN = Sum('NU_NOTA_CN'),
                SUM_NU_NOTA_CH = Sum('NU_NOTA_CH'),
                SUM_NU_NOTA_LC = Sum('NU_NOTA_LC'),
                SUM_NU_NOTA_MT = Sum('NU_NOTA_MT'),
                SUM_NU_NOTA_REDACAO = Sum('NU_NOTA_REDACAO')
                ).order_by('TP_COR_RACA')
        else:
            query_objects['TP_COR_RACA'] = Participant.objects.values('TP_COR_RACA').annotate(COUNT = Count('TP_COR_RACA')).order_by('TP_COR_RACA')
            query_objects['NU_NOTA'] = Participant.objects.values('TP_COR_RACA').annotate(
                SUM_NU_NOTA_CN = Sum('NU_NOTA_CN'),
                SUM_NU_NOTA_CH = Sum('NU_NOTA_CH'),
                SUM_NU_NOTA_LC = Sum('NU_NOTA_LC'),
                SUM_NU_NOTA_MT = Sum('NU_NOTA_MT'),
                SUM_NU_NOTA_REDACAO = Sum('NU_NOTA_REDACAO')
            ).order_by('TP_COR_RACA')
        participants = []
        for obj in query_objects['TP_COR_RACA']:
            for obj_sum in query_objects['NU_NOTA']:
                if (obj['TP_COR_RACA'] == obj_sum['TP_COR_RACA']):
                    participants.append({
                        "cor": titles[obj['TP_COR_RACA']],
                        "media": round(((obj_sum['SUM_NU_NOTA_CN'] / obj['COUNT']) + (obj_sum['SUM_NU_NOTA_CH'] / obj['COUNT']) + (obj_sum['SUM_NU_NOTA_LC'] / obj['COUNT']) + (obj_sum['SUM_NU_NOTA_MT'] / obj['COUNT']) + (obj_sum['SUM_NU_NOTA_REDACAO'] / obj['COUNT'])) / 5, 2)
                    })
                    break
        data = {
            'result': participants
        }
        return data

@ajax
@csrf_exempt
def dataPerformanceByInternetView(request):
    if (request.method == 'POST'):
        titles = {
            'A': "Não",
            'B': "Sim"
        }
        place = request.POST.get('place')
        query_objects = {}
        if(place != "BR"):
            query_objects['Q025'] = Participant.objects.filter(SG_UF_PROVA=place).values('Q025').annotate(COUNT = Count('Q025')).order_by('Q025')
            query_objects['NU_NOTA'] = Participant.objects.filter(SG_UF_PROVA=place).values('Q025').annotate(
                SUM_NU_NOTA_CN = Sum('NU_NOTA_CN'),
                SUM_NU_NOTA_CH = Sum('NU_NOTA_CH'),
                SUM_NU_NOTA_LC = Sum('NU_NOTA_LC'),
                SUM_NU_NOTA_MT = Sum('NU_NOTA_MT'),
                SUM_NU_NOTA_REDACAO = Sum('NU_NOTA_REDACAO')
            ).order_by('Q025')
        else:
            query_objects['Q025'] = Participant.objects.values('Q025').annotate(COUNT = Count('Q025')).order_by('Q025')
            query_objects['NU_NOTA'] = Participant.objects.values('Q025').annotate(
                SUM_NU_NOTA_CN = Sum('NU_NOTA_CN'),
                SUM_NU_NOTA_CH = Sum('NU_NOTA_CH'),
                SUM_NU_NOTA_LC = Sum('NU_NOTA_LC'),
                SUM_NU_NOTA_MT = Sum('NU_NOTA_MT'),
                SUM_NU_NOTA_REDACAO = Sum('NU_NOTA_REDACAO')
            ).order_by('Q025')
        participants = []
        for obj in query_objects['Q025']:
            for obj_sum in query_objects['NU_NOTA']:
                if (obj['Q025'] == obj_sum['Q025']):
                    participants.append({
                        "title": obj['Q025'],
                        "nota": round(((obj_sum['SUM_NU_NOTA_CN'] / obj['COUNT']) + (obj_sum['SUM_NU_NOTA_CH'] / obj['COUNT']) + (obj_sum['SUM_NU_NOTA_LC'] / obj['COUNT']) + (obj_sum['SUM_NU_NOTA_MT'] / obj['COUNT']) + (obj_sum['SUM_NU_NOTA_REDACAO'] / obj['COUNT'])) / 5, 2)
                    })
        data = {
            'result': participants
        }
        return data

@ajax
@csrf_exempt
def dataPerformanceByIncomeView(request):
    if (request.method == 'POST'):
        titles = {
            'A': 'Nenhuma renda.',
            'B': 'Até R$ 937,00.',
            'C': 'De R$ 937,01 até R$ 1.405,50.',
            'D': 'De R$ 1.405,51 até R$ 1.874,00.',
            'E': 'De R$ 1.874,01 até R$ 2.342,50.',
            'F': 'De R$ 2.342,51 até R$ 2.811,00.',
            'G': 'De R$ 2.811,01 até R$ 3.748,00.',
            'H': 'De R$ 3.748,01 até R$ 4.685,00.',
            'I': 'De R$ 4.685,01 até R$ 5.622,00.',
            'J': 'De R$ 5.622,01 até R$ 6.559,00.',
            'K': 'De R$ 6.559,01 até R$ 7.496,00.',
            'L': 'De R$ 7.496,01 até R$ 8.433,00.',
            'M': 'De R$ 8.433,01 até R$ 9.370,00.',
            'N': 'De R$ 9.370,01 até R$ 11.244,00.',
            'O': 'De R$ 11.244,01 até R$ 14.055,00.',
            'P': 'De R$ 14.055,01 até R$ 18.740,00.',
            'Q': 'Mais de R$ 18.740,00.'
        }
        place = request.POST.get('place')
        data = []
        query_objects = {}
        if (place != "BR"):
            query_objects['Q006'] = Participant.objects.filter(SG_UF_PROVA=place).values("Q006").annotate(COUNT=Count("Q006"))
            query_objects['NU_NOTA'] = Participant.objects.filter(SG_UF_PROVA=place).values('Q006').annotate(
                SUM_NU_NOTA_CN = Sum('NU_NOTA_CN'),
                SUM_NU_NOTA_CH = Sum('NU_NOTA_CH'),
                SUM_NU_NOTA_LC = Sum('NU_NOTA_LC'),
                SUM_NU_NOTA_MT = Sum('NU_NOTA_MT'),
                SUM_NU_NOTA_REDACAO = Sum('NU_NOTA_REDACAO')
            ).order_by('Q006')
        else:
            query_objects['Q006'] = Participant.objects.values("Q006").annotate(COUNT=Count("Q006"))
            query_objects['NU_NOTA'] = Participant.objects.values('Q006').annotate(
                SUM_NU_NOTA_CN = Sum('NU_NOTA_CN'),
                SUM_NU_NOTA_CH = Sum('NU_NOTA_CH'),
                SUM_NU_NOTA_LC = Sum('NU_NOTA_LC'),
                SUM_NU_NOTA_MT = Sum('NU_NOTA_MT'),
                SUM_NU_NOTA_REDACAO = Sum('NU_NOTA_REDACAO')
            ).order_by('Q006')          
        participants = []
        for obj in query_objects['Q006']:
            for obj_sum in query_objects['NU_NOTA']:
                if (obj['Q006'] == obj_sum['Q006']):
                    participants.append({
                        "title": titles[obj['Q006']],
                        "nota": round(((obj_sum['SUM_NU_NOTA_CN'] / obj['COUNT']) + (obj_sum['SUM_NU_NOTA_CH'] / obj['COUNT']) + (obj_sum['SUM_NU_NOTA_LC'] / obj['COUNT']) + (obj_sum['SUM_NU_NOTA_MT'] / obj['COUNT']) + (obj_sum['SUM_NU_NOTA_REDACAO'] / obj['COUNT'])) / 5, 2)
                    })
        data = {
            'result': participants
        }
        return data

@ajax
@csrf_exempt
def datacornumeroView(request):
    if (request.method == 'POST'):
        titles = {
            '0': 'Nao_declarado',
            '1': "Branca",
            '2': "Preta",
            '3': "Parda",
            '4': "Amarela",
            '5': "Indigena"
        }
        place = request.POST.get('place')
        
        if (place != "BR"):
            query_objects = Participant.objects.filter(SG_UF_PROVA=place).values('TP_COR_RACA').annotate(COUNT = Count('TP_COR_RACA')).order_by('TP_COR_RACA')
        else:
            query_objects = Participant.objects.values('TP_COR_RACA').annotate(COUNT = Count('TP_COR_RACA')).order_by('TP_COR_RACA')
        result = []
        for obj in query_objects:
            result.append({"title": titles[obj["TP_COR_RACA"]], "value": obj['COUNT']})
        data = {
            'result': result
        }
        return data

@ajax
@csrf_exempt
def info(request):
    return render(request, "website/info.html", {})
    
def index(request):
    data = {
      
    }
    return render(request, "website/index.html", data)