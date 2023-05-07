import requests
from django.shortcuts import render
from .models import Outfits


def home(request):
    outfit = None
    city = None
    clothes_type = None
    temp_celsius = None
    cold_outfits = Outfits.objects.filter(cold_weather_clothing__isnull=False)
    hot_outfits = Outfits.objects.filter(hot_weather_clothing__isnull=False)

    if request.method == 'POST':
        city = request.POST['city']

        URL = f'https://api.openweathermap.org/data/2.5/weather?q={city}&APPID=24cbe48a48d8bf0610dcd03339c6919a'
        response = requests.get(URL)
        data = response.json()

        try:
            temp_kelvin = data['main']['temp']
            temp_celsius = temp_kelvin - 273.15
            if temp_celsius <= 10:
                clothes_type = 'Thermal underwear, long-sleeve t-shirts, leggings, Fleece jackets, down vests, wool sweaters, This should be a perfect fit'
                outfit = cold_outfits.all()
            else:
                clothes_type = 'Cotton t-shirts, linen shirts, rayon dresses, Flowy skirts, sundresses, relaxed-fit shorts, This should be a perfect fit'
                outfit = hot_outfits.all()
        except KeyError:
            temp_celsius = None
            clothes_type = 'Invalid city name. Please try again.'

    context = {
        'outfit': outfit,
        'city': city,
        'clothes_type': clothes_type,
        'temp_celsius': temp_celsius
    }

    return render(request, 'home.html', context)
