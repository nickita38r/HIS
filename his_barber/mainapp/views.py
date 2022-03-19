from django.shortcuts import render

from django.views.generic import DetailView, View
from matplotlib.style import context

from .models import (
    ServiceType,
    SpecialOffer,
    Question,
    Barber,
    GalaryHairstyle
)

class BaseView(View):

    def get(self, request, *args, **kwargs):
        types = ServiceType.objects.all()
        offer = SpecialOffer.objects.all()
        barber = Barber.objects.all()
        questions = Question.objects.all()
        image_hearstyle = [x for x in GalaryHairstyle.objects.all() if x.chek]
        context = {
            'types':types,
            'offers': offer,
            'barbers': barber,
            'hearstyle': image_hearstyle,
            'qustionLeft': questions[:int(len(questions)/2)],
            'qustionRight': questions[int(len(questions)/2):],
        }
        return render(request, 'base.html', context)

class BarberView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'barber.html', context = {'barbers':Barber.objects.all()})