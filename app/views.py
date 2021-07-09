import pickle

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse
from django.utils.translation import ugettext as _, activate
# Create your views here.

from django.http import HttpResponse
from app.models import Person
# def index(request):
#     d = ''
#     a = Person.objects.all()
#     for i in a:
#        d = d + i.name + ' '
#     return HttpResponse(d)
from django.conf import settings


def index(request):
    context = {
    'Person3': Person.objects.filter(id=3)[0]
    }
    return render(request, 'index.html', context)

def about(request):
    context = {

    }
    return render(request, 'about.html', context)

def contacts(requesr):
    return HttpResponse('Андрей, тел. +375336002288')

def login_users(request):
    user = authenticate(
        username=request.POST['username'],
        password=request.POST['password']
    )
    if user is None:
        return render(request, 'error.html', {})
    else:
        login(request, user)
        return HttpResponseRedirect('index')

def do_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('index')

def registration(request):
    return render(request, 'registration.html')

def england(request):
    return render(request, 'england.html')

def register(request):
    user = User.objects.create_user(
        request.POST['login'],
        # username=request.POST['username'],
        password=request.POST['password'],
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email']
    )
    return HttpResponse('Ok')

def ajax_1(request):
    response = {
        'message': 15
    }
    return JsonResponse(response)

def login_1(request):
    if len(User.objects.filter(username=request.POST['aaa'])) == 0:
        exists = 'n'
    else:
        exists = 'y'
    response = {
        'exists': exists
    }
    return JsonResponse(response)


import requests
import json

def nbrb_rate(request):
    def rate():
        response = requests.get('https://www.nbrb.by/api/exrates/rates/dynamics/145?startdate=2021-06-20&enddate=2021-06-26')
        price = json.loads(response.text)
        rate_sum = 0
        for i in price:
            rate = i['Cur_OfficialRate']
            rate_sum += rate
            average_rate = round(rate_sum / 7, 3)
        return average_rate
    # rate()
    # return HttpResponse("Средний курс за последние 7 дней " + str(rate()))
    return render(request, 'common.html', {'a': rate()})





import random
from datetime import datetime
from app.models import Person_1

def experiment(request):
    size = 300000
    slice_size = 500
    Person_1.objects.all().delete()
    for _ in range(int(size / slice_size)):
        slice = []
        for _ in range(slice_size):
            slice.append(
                Person_1(
                    name=str(random.randint(1, 1500)),
                    credit_card_number=str(
                        random.randint(10**70, 10**80)
                    )
                )
            )
        Person_1.objects.bulk_create(slice, slice_size)

    sum = 0
    for _ in range(100):
        start = datetime.now()
        list(Person_1.objects.filter(
            credit_card_number=random.randint(
                10**70, 10**80
            )
        ))
        delta = (datetime.now() - start).total_seconds()
        sum = sum + delta
    print("Время выполнения 100 запрсосов: " +
          str(sum) + ' секунд')

    return HttpResponse('Ok')


def translate(request):
    # activate('en-en')
    response = HttpResponseRedirect('index')
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, 'en-en')
    return response

    #     render(request,
    #     'index.html',
    #     {'title': _('Под действием гидроксиламина альдегиды превращаются в оксимы:')}
    # )


import pickle
from pymemcache import Client
from app.models import Person

# def main(request):
#     client = Client(('localhost', 11211))
#     people = client.get('people')
#     if people is None:
#         people = []
#         for person in Person.objects.all()[:5]:
#             people.append(person.name)
#         client.set(
#             'people',
#             pickle.dumps(people),
#             expire=60
#         )
#     else:
#         people = pickle.loads(people)
#     return render(
#         request,
#         'index.html',
#         {
#             'people': people
#         }
#     )


def server(request):
    if 'id' in request.POST:
        Person.objects.filter(
            id=request.POST['id']
        ).update(
            age=int(request.POST['age'])
        )
        return JsonResponse({'status': 'Ok'})
    else:
        spisok = []
        id = request.GET['id']
        Person.objects.filter(id=id)
        for i in Person.objects.filter(id=id):
            spisok.append({
                'name': i.name,
                'age': i.age
            })
        return JsonResponse({'status': 'Ok'})
