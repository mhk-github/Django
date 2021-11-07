###############################################################################
# FILE     : weather_view.py
# SYNOPSIS : A specific Django 3 class-view to obtain the weather.
# LICENSE  : MIT
###############################################################################


###############################################################################
# IMPORTS
###############################################################################

import requests

from django.conf import settings
from django.http import JsonResponse
from django.views import View


###############################################################################
# CLASSES
###############################################################################

class WeatherView(View):
    """Class-based view to get weather data."""

    def get(self, request):
        """Returns JSON for integer temperature in Celsius at a location."""

        location = request.GET.get('q', None)
        if location:
            query = {
                'appid': settings.OPENWEATHERMAP_API_KEY,
                'q': location
            }
            response = requests.get(
                settings.OPENWEATHERMAP_URL_WEATHER,
                params=query,
                timeout=settings.OPENWEATHERMAP_TIMEOUT
            )
            response_json = response.json()
            temperature = settings.ABSOLUTE_ZERO_IN_CELSIUS
            if response_json['cod'] != '404':
                main_info = response_json['main']
                temperature = round(
                    float(main_info['temp']) - settings.ZERO_CELSIUS_IN_KELVIN
                )
                
            return JsonResponse({'temperature': temperature})


###############################################################################
# END
###############################################################################
# Local variables:
# mode: python
# End:
