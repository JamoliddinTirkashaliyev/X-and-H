from django.shortcuts import render
from .models import *

def index(request):
    search = request.GET.get("search")
    togriSozlar = TogriSoz.objects.filter(soz=search)
    if togriSozlar and search:
        togriSoz = togriSozlar[0]
        notogriSoz = NotogriSoz.objects.filter(togriSoz=togriSoz)

        context = {
            'togriSoz': togriSoz,
            'notogriSoz': notogriSoz
        }
        return render(request, 'index.html', context)
    elif search:
        notogriSoz = NotogriSoz.objects.filter(soz=search).first()
        if notogriSoz:
            togriSoz = TogriSoz.objects.get(id = notogriSoz.togriSoz.id)
            notogriSoz = NotogriSoz.objects.filter(togriSoz=togriSoz)
            print(togriSoz),
            print(notogriSoz),
            context = {
                'togriSoz': togriSoz,
                'notogriSoz': notogriSoz,
            }
            #return render(request, 'index.html', context)

        else:
            context = {
                 'togriSoz':'Mavjut emas!',
                 'notogriSoz': ['Mavjut emas!'],
             }
        return render(request, 'index.html', context)
    elif search == '':
        context = {
            'togriSoz': "So'z kiriting!",
            'notogriSoz': ["So'z kiriting!"],
        }
        return render(request, 'index.html', context)



    return render(request, 'index.html')
