import csv
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('phones.csv', 'r', encoding='utf-8') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for row in phones:
            Phone.objects.update_or_create(
                id=int(row['id']),
                defaults={
                    'name': row['name'],
                    'price': float(row['price']),
                    'image': row['image'],
                    'release_date': row['release_date'],
                    'lte_exists': row['lte_exists'] == 'True',
                },
            )
        self.stdout.write(self.style.SUCCESS(f'Импортировано: {len(phones)}'))