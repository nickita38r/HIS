from tkinter.messagebox import QUESTION
from django.contrib import admin
from .models import *

admin.site.register(ServiceType)
admin.site.register(ServiceAlbum)
admin.site.register(SpecialOffer)
admin.site.register(Question)
admin.site.register(Barber)
admin.site.register(GalaryHairstyle)

