# Generated by Django 4.0.2 on 2022-03-11 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='SpecialOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceAlbum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('priceBarber', models.IntegerField()),
                ('priceBigBarber', models.IntegerField()),
                ('priceTopBarber', models.IntegerField()),
                ('kind', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.servicetype')),
            ],
        ),
    ]
