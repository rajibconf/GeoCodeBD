"""geoCodeBD_app > scripts.py"""
import csv
# DJANGO IMPORTS

# APP IMPORTS
from geoCodeBD_app.models import (
    Division, District, Upazila,
    Union, Village
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
    usr_list = [
        'DoesNotExist', 'Meta', 'MultipleObjectsReturned', 'REQUIRED_FIELDS', 'USERNAME_FIELD', '__class__',
        '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
        '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__',
        '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__',
        '__str__', '__subclasshook__', '__weakref__', '_check_column_name_clashes', '_check_constraints',
        '_check_field_name_clashes', '_check_fields', '_check_id_field', '_check_index_together', '_check_indexes',
        '_check_local_fields', '_check_long_column_names', '_check_m2m_through_same_relationship', '_check_managers',
        '_check_model', '_check_model_name_db_lookup_clashes', '_check_ordering',
        '_check_property_name_related_field_accessor_clashes', '_check_single_primary_key', '_check_swappable',
        '_check_unique_together', '_do_insert', '_do_update', '_get_FIELD_display', '_get_next_or_previous_by_FIELD',
        '_get_next_or_previous_in_order', '_get_pk_val', '_get_unique_checks', '_legacy_get_session_auth_hash',
        '_meta', '_password', '_perform_date_checks', '_perform_unique_checks', '_save_parents', '_save_table',
        '_set_pk_val', 'auth_token', 'check', 'check_password', 'clean', 'clean_fields', 'date_error_message',
        'date_joined', 'delete', 'district_set', 'division_set', 'email', 'first_name', 'from_db', 'full_clean',
        'get_all_permissions', 'get_deferred_fields', 'get_email_field_name', 'get_full_name',
        'get_group_permissions', 'get_phone_intl_format', 'get_session_auth_hash', 'get_user_permissions',
        'get_username', 'groups', 'has_module_perms', 'has_perm', 'has_perms', 'has_usable_password', 'id',
        'is_active', 'is_anonymous', 'is_authenticated', 'is_staff', 'is_superuser', 'last_login', 'last_name',
        'last_updated', 'logentry_set', 'natural_key', 'normalize_username', 'objects', 'password', 'phone', 'pk',
        'prepare_database_save', 'profile', 'refresh_from_db', 'save', 'save_base', 'serializable_value',
        'set_password', 'set_unusable_password', 'union_set', 'unique_error_message', 'upazila_set',
        'user_permissions', 'validate_unique', 'village_set'
    ]
    users = User.objects.all()
    for obj in users:
        print(f"{obj.email}")


# get_fields()

# comment