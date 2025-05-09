import requests
from django.core.management.base import BaseCommand
from countries.models import Country

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        url = "https://restcountries.com/v3.1/all"
        response = requests.get(url)
        for item in response.json():
            Country.objects.update_or_create(
                cca2=item.get('cca2', ''),
                defaults={
                    'name': item.get('name', {}).get('common', ''),
                    'capital': item.get('capital', [''])[0],
                    'population': item.get('population', 0),
                    'region': item.get('region', ''),
                    'timezone': item.get('timezones', [''])[0],
                    'flag': item.get('flags', {}).get('png', ''),
                    'languages': item.get('languages', {})
                }
            )
        self.stdout.write("Countries fetched and saved.")
