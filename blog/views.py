from django.shortcuts import render
from django.http import HttpResponse
import datetime
from . import models

def cinemaView(request):
    cinema_value = models.Cinema.objects.all()
    return render(request, 'cinema/cinema.html', {'cinema_key': cinema_value})


# def cinemaView(request):
#     cinema_value = models.Cinema.objects.all()
#     html_cinema = 'cinema/cinema.html'
#     context = {
#         'cinema_key': cinema_value,
#
#     }
#     return render(request,html_cinema, context)




def helloView(request):
    return HttpResponse("<h1>Hello! It's my project</h1>")

def dateView(request):
    date = datetime.date.today()
    return HttpResponse(f"<h1>{date}</h1>")

def byeView(request):
    return HttpResponse("<h1>Goodby user!</h1>")

