"""geoCodeBD_app > models > division.py"""
# DJANGO IMPORTS
from django.db import models
from django.utils.translation import gettext_lazy as _
# APP IMPORTS
from geoCodeBD_app.models import CommonFieldModel


class Division(CommonFieldModel):
    """Division model"""
    name = models.CharField(
        _('বিভাগের নাম ইংরেজিতে'), max_length=100,
        unique=True, blank=False, null=True
    )
    bn_name = models.CharField(
        _('বিভাগের নাম বাংলায়'), max_length=100,
        unique=True, blank=False, null=True
    )
    code = models.CharField(
        _('বিভাগের কোড'), max_length=10,
        blank=False, null=True
    )
    latitude = models.CharField(
        max_length=50, blank=True, null=True
    )
    longitude = models.CharField(
        max_length=50, blank=True, null=True
    )
    url = models.CharField(
        _('ওয়েবসাইটের ঠিকানা'), max_length=120,
        unique=True, blank=False, null=True
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.bn_name
