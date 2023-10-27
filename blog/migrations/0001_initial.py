# Generated by Django 4.2.6 on 2023-10-23 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField()),
                ('type_film', models.CharField(choices=[('хоррор', 'хоррор'), ('фантастика', 'фантастика'), ('приключения', 'приключения'), ('боевик', 'боевик')], max_length=100)),
                ('year', models.DateField(verbose_name='дата созадния:')),
            ],
        ),
    ]