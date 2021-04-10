"""geoCodeBD_app > scripts.py"""
import csv
# DJANGO IMPORTS

# APP IMPORTS
from geoCodeBD_app.models import (
    Division, District, Upazila,
    Union
)
from Core.models import User


def division():
    with open(
            '/home/mohammadrajib/Desktop/GeoCodeBD/fixtures/add/divisions.csv'
    ) as f:
        reader = csv.reader(f)
        num = 0
        for row in reader:
            obj, created = Division.objects.get_or_create(
                pk=row[0],
                name=row[1],
                bn_name=row[2],
                url=row[3],
            )
            num += 1
            print(f'SlN={num}, object={obj}, created={created}')


# division()


def district():
    with open(
            '/home/mohammadrajib/Desktop/GeoCodeBD/fixtures/add/districts.csv'
    ) as f:
        reader = csv.reader(f)
        num = 0
        for row in reader:
            obj, created = District.objects.get_or_create(
                pk=row[0],
                division=Division.objects.get(id=row[1]),
                name=row[2],
                bn_name=row[3],
                latitude=row[4],
                longitude=row[5],
                url=row[6],
            )
            num += 1
            print(f'SlN={num}, object={obj}, created={created}')


# district()


def upazila():
    with open(
            '/home/mohammadrajib/Desktop/GeoCodeBD/fixtures/add/upazilas.csv'
    ) as f:
        reader = csv.reader(f)
        num = 0
        for row in reader:
            obj, created = Upazila.objects.get_or_create(
                pk=row[0],
                district=District.objects.get(id=row[1]),
                name=row[2],
                bn_name=row[3],
                url=row[4],
            )
            num += 1
            print(f'SlN={num}, object={obj}, created={created}')


# upazila()


def union():
    with open(
            '/home/mohammadrajib/Desktop/GeoCodeBD/fixtures/add/unions.csv'
    ) as f:
        reader = csv.reader(f)
        num = 0
        for row in reader:
            obj, created = Union.objects.get_or_create(
                pk=row[0],
                upazila=Upazila.objects.get(id=row[1]),
                name=row[2],
                bn_name=row[3],
                url=row[4],

            )
            num += 1
            print(f'num={num}, object={obj}, created={created}')


# union()


# get fields
def get_fields():
    # villages = Village._meta.get_fields()
    # for field in villages:
    #     print(field)
    # print(Village._meta.get_fields())
    # print('\n')
    # print(User._meta.get_fields())
    # print(dir(User))
    users = User.objects.all()
    for obj in users:
        print(f"{obj.email}")

# get_fields()
