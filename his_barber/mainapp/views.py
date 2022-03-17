from django.shortcuts import render

from django.views.generic import DetailView, View

from .models import (
    ServiceType,
    ServiceAlbum,
    SpecialOffer,
    Question,
)

class BaseView(View):



    def get(self, request, *args, **kwargs):
        init = {}
        types = ServiceType.objects.all()
        album = ServiceAlbum.objects.all()
        offer = SpecialOffer.objects.all()
        questions = Question.objects.all()
        for name in types: init[str(name.name)] = [x for x in album if x.kind.name == name.name]
        print(init)
        context = {
            'perem':[123456],
            'types' : [x.name for x in ServiceType.objects.all()],
            'album': init,
            'offers': offer,
            'qustionLeft': questions[:int(len(questions)/2)],
            'qustionRight': questions[int(len(questions)/2):],
        }
        return render(request, 'base.html', context)

