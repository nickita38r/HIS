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
        types = ServiceType.objects.all()
        album = ServiceAlbum.objects.all()
        offer = SpecialOffer.objects.all()
        questions = [x for x in Question.objects.all()]
        context = {
            'type' : types,
            'album': album,
            'offers': offer,
            'qustionLeft': questions[:int(len(questions)/2)],
            'qustionRight': questions[int(len(questions)/2):],
        }
        return render(request, 'base.html', context)
