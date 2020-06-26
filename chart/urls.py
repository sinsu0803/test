from django.contrib import admin
from django.urls import path
from chart import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('covid-191/', views.covid_191, name='covid_191'),
    path('covid-192/', views.covid_192, name='covid_192'),
    path('covid-193/', views.covid_193, name='covid_193'),
    path('ticket_class/', views.ticket_class, name='ticket_class'),
]