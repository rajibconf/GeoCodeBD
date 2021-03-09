"""geoCodeBD_app > models > union.py"""
# DJANGO IMPORTS
from django.db import models
from django.utils.translation import gettext_lazy as _
# APP IMPORTS
from geoCodeBD_app.models import CommonFieldModel, Upazila


class Union(CommonFieldModel):
    """Union model"""
    upazila = models.ForeignKey(
        Upazila, on_delete=models.SET_NULL, blank=False,
        null=True, verbose_name='উপজেলা'
    )
    name = models.CharField(
        _('ইউনিয়নের নাম ইংরেজিতে'), max_length=100,
        blank=False, null=True
    )
    bn_name = models.CharField(
        _('ইউনিয়নের নাম বাংলায়'), max_length=100,
        blank=False, null=True
    )
    code = models.CharField(
        _('ইউনিয়নের কোড'), max_length=10,
        blank=True, null=True
    )
    latitude = models.CharField(
        max_length=50, blank=True, null=True
    )
    longitude = models.CharField(
        max_length=50, blank=True, null=True
    )
    url = models.CharField(
        _('ওয়েবসাইটের ঠিকানা'), max_length=120,
        blank=True, null=True
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
