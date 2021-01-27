from django.shortcuts import render
import requests

def home(request):
    return render(request, 'home.html')

def airquality(request):
    city = request.GET['city']
    country = request.GET['country']
    response = requests.get('https://api.weatherbit.io/v2.0/current/airquality?city='+city+'&country='+country+'&key=952b420969c0482d856ae42e392f5bcf')
    data = response.json()
    aqi = int(data['data'][0]['aqi'])
    
    if aqi>=0 and aqi<=50:
        aqi_level = "Good" #Green
        aqi_level_color = "green"
        aqi_description = "Air quality is satisfactory, and air pollution poses little or no risk."

    if aqi>=51 and aqi<=100:
        aqi_level = "Moderate" #Yellow
        aqi_level_color = "yellow"
        aqi_description = "Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."

    if aqi>=101 and aqi<=150:
        aqi_level = "Unhealthy for sensitive groups" #Orange
        aqi_level_color = "orange"
        aqi_description = "Members of sensitive groups may experience health effects. The general public is less likely to be affected."

    if aqi>=151 and aqi<=200:
        aqi_level = "Unhealthy" #red
        aqi_level_color = "red"
        aqi_description = "Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."

    if aqi>=201 and aqi<=300:
        aqi_level = "Very unhealthy" #purple
        aqi_level_color = "purple"
        aqi_description = "Health alert: The risk of health effects is increased for everyone."

    if aqi>=301 and aqi<=500:
        aqi_level = "Hazardous" #Maroon
        aqi_level_color = "maroon"
        aqi_description = "Health warning of emergency conditions: everyone is more likely to be affected."

    aqi_percentage = (aqi*100/500)/100
    print("AQI :", aqi_percentage)

    return render(request, 'airquality.html', {
        'city_name':data['city_name'],
        'lat': data['lat'],
        'lon':data['lon'],
        'country':data['country_code'],
        'air_quality_index':data['data'][0]['aqi'],
        'ozone_conc':data['data'][0]['o3'],
        'sul_dioxide_conc': data['data'][0]['so2'],
        'nitro_dioxide_conc':data['data'][0]['no2'],
        'carb_monoxide':data['data'][0]['co'],
        'pm10':data['data'][0]['pm10'],
        'pm25': data['data'][0]['pm25'],
        'mold_level': data['data'][0]['mold_level'],
        'aqi_percentage':aqi_percentage,
        'aqi_level': aqi_level,
        'aqi_level_color': aqi_level_color,
        'aqi_description': aqi_description,
    })