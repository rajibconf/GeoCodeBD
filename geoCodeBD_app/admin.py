"""geoCodeBD_app > admin.py"""
# DJANGO IMPORTS
from django.contrib import admin
# APP IMPORTS
from geoCodeBD_app.models import (
    Division, District, Upazila,
    Union, Village
)


@admin.register(Division)
class DivisionModelAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'bn_name', 'code',
        'url',
        # 'created_at', 'updated_at',
        'is_active'
    ]
    list_filter = [
        'is_active'
    ]
    search_fields = [
        'name', 'bn_name', 'url'
    ]
    ordering = [
        'name', 'bn_name'
    ]
    # readonly_fields = (
    #     'created_at', 'updated_at'
    # )


@admin.register(District)
class DistrictModelAdmin(admin.ModelAdmin):
    list_display = [
        'division', 'name', 'bn_name', 'code',
        # 'created_at', 'updated_at',
        'is_active'
    ]
    list_filter = [
        'is_active', 'division'
    ]
    search_fields = [
        'name', 'bn_name', 'url'
    ]
    ordering = [
        'name', 'bn_name'
    ]
    # readonly_fields = ('created_at', 'updated_at')


@admin.register(Upazila)
class UpazilaModelAdmin(admin.ModelAdmin):
    list_display = [
        'district', 'name', 'bn_name', 'code',
        # 'created_at', 'updated_at',
        'is_active'
    ]
    list_filter = [
        'is_active', 'district'
    ]
    search_fields = [
        'name', 'bn_name', 'url'
    ]
    ordering = [
        'name', 'bn_name'
    ]
    # readonly_fields = ('created_at', 'updated_at')


@admin.register(Union)
class UnionModelAdmin(admin.ModelAdmin):
    list_display = [
        'upazila', 'name', 'bn_name', 'code',
        # 'created_at', 'updated_at',
        'is_active'
    ]
    list_filter = [
        'is_active', 'upazila'
    ]
    search_fields = [
        'name', 'bn_name', 'url'
    ]
    ordering = [
        'name', 'bn_name'
    ]
    # readonly_fields = ('created_at', 'updated_at')


@admin.register(Village)
class VillageModelAdmin(admin.ModelAdmin):
    list_display = [
        'union', 'name', 'bn_name', 'code',
        # 'created_at', 'updated_at',
        'is_active'
    ]
    list_filter = [
        'is_active', 'union'
    ]
    search_fields = [
        'name', 'bn_name', 'url'
    ]
    ordering = [
        'name', 'bn_name'
    ]
    # readonly_fields = ('created_at', 'updated_at')
