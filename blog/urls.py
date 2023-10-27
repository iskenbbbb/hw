from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.helloView),
    path('date/', views.dateView),
    path('bye/', views.byeView),
    path('cinema/', views.cinemaView),
]