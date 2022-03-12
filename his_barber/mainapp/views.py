from django.shortcuts import render

from django.views.generic import DetailView, View

from .models import (
    ServiceType,
    ServiceAlbum,
    SpecialOffer,
)

class BaseView(View):

    def get(self, request, *args, **kwargs):
        types = ServiceType.objects.all()
        album = ServiceAlbum.objects.all()
        offer = SpecialOffer.objects.all()
        context = {
            'type' : types,
            'album': album,
            'offers': offer
        }
        return render(request, 'base.html', context)
