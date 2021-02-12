# python3 manage.py runscript many_load
import csv
from unesco.models import Category, Iso, Region, Site, States


def run():

    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.DictReader(fhand)

    Category.objects.all().delete()
    Iso.objects.all().delete()
    Region.objects.all().delete()
    Site.objects.all().delete()
    States.objects.all().delete()

    for row in reader:
        c, _ = Category.objects.get_or_create(name=row['category'])
        i, _ = Iso.objects.get_or_create(name=row['iso'])
        r, _ = Region.objects.get_or_create(name=row['region'])
        s, _ = States.objects.get_or_create(name=row['states'])
        site = Site(
            name = row['name'],
            description = row['description'],
            justification = row['justification'],
            year = int(row['year']) if row['year'] != '' else None,
            category = c,
            longitude = float(row['longitude']) if row['longitude'] != '' else None,
            latitude = float(row['latitude']) if row['latitude'] != '' else None,
            area_hectares = float(row['area_hectares']) if row['area_hectares'] != '' else None,
            states = s,
            region = r,
            iso = i
        )
        site.save()
