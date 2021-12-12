import csv
from django.template.defaultfilters import slugify
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            # TODO: Добавьте сохранение модели
            reader = Phone.objects.create(id=int(phone[0]), name=int(phone[1]),
                                          price=int(phone[3]), image=phone[2],
                                          release_data=int(phone[4]), Ite_existe=phone[5],
                                          slug=slugify(phone[1]),
                                          )
            pass
