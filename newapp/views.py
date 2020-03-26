from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
# Create your views here.
def statistics(request):
    response = requests.get('https://api.covid19api.com/summary')
    data1 = response.json()
    Countries = data1['Countries']
    country_name = {}
    if 'country' in request.GET:
        country_name = request.GET['country']
        print(country_name)
        Found = False
        for i in Countries:
            if (i['Country'] == country_name) or (i['Slug'] == country_name):
                Total_Confirmed =    i['TotalConfirmed']
                New_Confirmed   =    i['NewConfirmed']
                New_Deaths      =    i['NewDeaths']
                Total_Deaths    =    i['TotalDeaths']
                New_Recovered   =    i['NewRecovered']
                Total_Recovered =    i['TotalRecovered']
                return render(request,'Results.html',{
                'country':country_name,
                'TotalConfirmed':Total_Confirmed,
                'NewConfirmed':New_Confirmed,
                'TotalDeaths':Total_Deaths,
                'NewDeaths':New_Deaths,
                'NewRecovered':New_Recovered,
                'TotalRecovered':Total_Recovered,})
                return render(request,'Results.html',{
                'TotalConfirmed':Total_Confirmed
                })
                break
        else:
            Total_Confirmed =    0
            New_Confirmed   =    0
            New_Deaths      =    0
            Total_Deaths    =    0
            New_Recovered   =    0
            Total_Recovered =    0
            return render(request,'Results.html',{
            'country':country_name,
            'TotalConfirmed':Total_Confirmed,
            'NewConfirmed':New_Confirmed,
            'TotalDeaths':Total_Deaths,
            'NewDeaths':New_Deaths,
            'NewRecovered':New_Recovered,
            'TotalRecovered':Total_Recovered,})
            return render(request,'Results.html',{
            'TotalConfirmed':Total_Confirmed
            })
    return render(request,'corona.html',{
    'country':country_name
    })
