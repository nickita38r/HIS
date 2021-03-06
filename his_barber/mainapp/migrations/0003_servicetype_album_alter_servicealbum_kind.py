# Generated by Django 4.0.2 on 2022-03-11 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_alter_servicealbum_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicetype',
            name='album',
            field=models.ManyToManyField(blank=True, related_name='related_Album', to='mainapp.ServiceAlbum'),
        ),
        migrations.AlterField(
            model_name='servicealbum',
            name='kind',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.servicetype', verbose_name='Тип услуги'),
        ),
    ]
