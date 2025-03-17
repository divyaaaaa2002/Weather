from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    city=request.GET.get('city','bengaluru')
    api_url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=69c9c23c96101a6c9674babb22b7ec39&units=metric"

    api=requests.get(api_url).json()
    temperature=api['main']['temp']
    country=api['sys']['country']
    city_name=api['name']
    return render(request,"index.html",{'temperature':temperature,"country":country,"city":city_name})
