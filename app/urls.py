from django.urls import path
from app.views import *

urlpatterns = [
    path('', index),
    path('index', index),
    path('about', about),
    path('contacts', contacts),
    path('login', login_users),
    path('logout', do_logout),
    path('registration', registration),
    path('registr', register),
    path('england', england),
    path('ajax_1', ajax_1),
    path('log_2', login_1),
    path('rate', nbrb_rate),
    path('experiment', experiment),
    path('translate', translate),
    path('person', server)
]