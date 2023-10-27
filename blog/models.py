from django.db import models
from blog.constants import FILM_TYPE


class Hashtag(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Хештег'
        verbose_name_plural = 'Хештеги'


class Cinema(models.Model):
    """ref"""
    hashtags = models.ManyToManyField(Hashtag)

    title = models.CharField(max_length=100, verbose_name='название фильма', null=True)
    # image = models.ImageField(upload_to='', verbose_name='вставьте постер фильма', null=True)
    description = models.TextField(blank=True, verbose_name='описание фильма', null=True)
    type_film = models.CharField(max_length=100, choices=FILM_TYPE, verbose_name='каддите жанр', null=True)
    year = models.DateField(verbose_name='дата созадния:', null=True)
    creator = models.CharField(max_length=100, verbose_name='укажите автора', null=True)
    created_at = models.DateTimeField(auto_created=True, null=True)

    def __str__(self):
        return f'название: {self.title}\n' \
               f'создатель: {self.creator}'

    class Meta:
        verbose_name = 'фильм'
        verbose_name_plural = 'фильмы'
