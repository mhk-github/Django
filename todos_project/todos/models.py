###############################################################################
# IMPORTS
###############################################################################

import requests

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from .weather import (
    API_KEY,
    BASE_URL_WEATHER,
    ZERO_C_IN_K,
)


###############################################################################
# CLASSES
###############################################################################

class Todo(models.Model):
    MELBOURNE = 'Melbourne'
    LONDON = 'London'
    NEW_YORK = 'New York'
    PARIS = 'Paris'
    VLADIVOSTOK ='Vladivostok'
    CITY_CHOICES = [
        (MELBOURNE, 'Melbourne'),
        (LONDON, 'London'),
        (NEW_YORK, 'New York'),
        (PARIS, 'Paris'),
        (VLADIVOSTOK, 'Vladivostok'),
    ]
    
    task = models.CharField(max_length=255, unique_for_date='created')
    location = models.CharField(max_length=255, choices=CITY_CHOICES)
    temperature = models.FloatField()
    done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return(
            '<class Todo: '
            f"id={self.id} "
            f"task='{self.task}' "
            f"location='{self.location}' "
            f"temperature={self.temperature}C "
            f"done={self.done} "
            f"created={self.created} "
            f"updated={self.updated} "
            '>'
        )


###############################################################################
# CALLBACKS
###############################################################################

@receiver(pre_save)
def pre_save_callback(sender, instance, *args, **kw_args):
    if 'Todo' in f"{sender}":
        url_weather = (
            f"{BASE_URL_WEATHER}appid={API_KEY}&q={instance.location}"
        )
        response = requests.get(url_weather)
        response_json = response.json()
        if response_json['cod'] != '404':
            main_info = response_json['main']
            current_temperature = float(main_info['temp']) - ZERO_C_IN_K
            instance.temperature = current_temperature

