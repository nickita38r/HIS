# Generated by Django 4.0.2 on 2022-03-16 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_servicetype_album_alter_servicealbum_kind'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Вопрос')),
                ('answer', models.TextField(verbose_name='Ответ')),
            ],
        ),
        migrations.RemoveField(
            model_name='servicetype',
            name='album',
        ),
    ]
