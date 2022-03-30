from django.db import models
from django.urls import reverse

class ServiceType(models.Model):
    name = models.CharField(max_length=30, verbose_name='Тип услуги')
    def __str__(self):
        return f'{self.name}'

class ServiceAlbum(models.Model):
    kind = models.ForeignKey(ServiceType, on_delete=models.CASCADE, verbose_name = 'Тип услуги', related_name='price')
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

class Question(models.Model):
    title = models.CharField(max_length=100, verbose_name='Вопрос')
    answer = models.TextField(verbose_name='Ответ')
    def __str__(self):
        return f'{self.title}'

class Barber(models.Model):
    image = models.ImageField(verbose_name='Аватарка')
    firstName = models.CharField(max_length=30, verbose_name='Имя')
    lastName = models.CharField(max_length=30, verbose_name='Фамилия')
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return f'{self.firstName} {self.lastName}'

    def get_absolute_url(self):
        return reverse('barber_detail', kwargs={'slug': self.slug})

class GalaryHairstyle(models.Model):
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE, verbose_name = 'Барбер', related_name='galary')
    chek = models.BooleanField(default=False)
    image = models.ImageField(verbose_name='Фото')

class Review(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    data = models.DateField(verbose_name="Дата")
    starts = models.IntegerField(verbose_name="Колличество звезд")
    text = models.TextField(verbose_name="Отзыв")

    def __str__(self):
        return f'{self.name}'