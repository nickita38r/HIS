from django.db import models

class ServiceType(models.Model):
    name = models.CharField(max_length=30, verbose_name='Тип услуги')
    def __str__(self):
        return f'{self.name}'

class ServiceAlbum(models.Model):
    kind = models.ForeignKey(ServiceType, on_delete=models.CASCADE, verbose_name = 'Тип услуги')
    name = models.CharField(max_length=50, verbose_name = 'Наименование услуги')
    priceBarber = models.IntegerField(verbose_name = 'Цена барбера')
    priceBigBarber = models.IntegerField(verbose_name = 'Цена старшего барбера')
    priceTopBarber = models.IntegerField(verbose_name = 'Цена ТОП барбера')

    def __str__(self):
        return f'{self.name}'

class SpecialOffer(models.Model):
    offer = models.CharField(max_length=200, verbose_name='Cпециальное предложение')
    def __str__(self):
        return f'{self.offer}'