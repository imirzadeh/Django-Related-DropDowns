from django.shortcuts import render
from map.models import *
import json as simplejson
from django.http import HttpResponse
# Create your views here.


def index(request):

    countries = Country.objects.all()
    print(countries)
    return render(request, 'index.html', {'countries': countries})


def getdetails(request):

    #country_name = request.POST['country_name']
    country_name = request.GET['cnt']
    print("ajax " + str(country_name))

    result_set = []
    all_cities = []

    answer = str(country_name[1:-1])
    selected_country = Country.objects.get(name=answer)
    print("selected country name " + str(selected_country))

    all_cities = selected_country.city_set.all()
    for city in all_cities:
        print("city name" + str(city.name))
        result_set.append({'name': city.name})

    return HttpResponse(simplejson.dumps(result_set), content_type='application/json')
