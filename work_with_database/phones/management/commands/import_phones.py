import csv
from datetime import datetime

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', newline='') as csvfile:
            phone_reader = csv.DictReader(csvfile, delimiter=";")

            for line in phone_reader:
                p = Phone(
                    id=line.get('id'),
                    name=line.get('name'),
                    image=line.get('image'),
                    price=line.get('price'),
                    release_date=datetime.strptime(line.get('release_date'), "%Y-%m-%d").date(),
                    slug=line.get('name').replace(' ', '_')
                )
                p.save()
