"""geoCodeBD_app > models > village.py"""
# DJANGO IMPORTS
from django.db import models
from django.utils.translation import gettext_lazy as _
# APP IMPORTS
from geoCodeBD_app.models import CommonFieldModel, Union


class Village(CommonFieldModel):
    """Village model"""
    union = models.ForeignKey(
        Union, on_delete=models.SET_NULL, blank=False,
        null=True, verbose_name='ইউনিয়ন'
    )
    name = models.CharField(
        _('গ্রামের নাম ইংরেজিতে'), max_length=100,
        blank=False, null=True
    )
    bn_name = models.CharField(
        _('গ্রামের নাম বাংলায়'), max_length=100,
        blank=False, null=True
    )
    code = models.CharField(
        _('গ্রামের কোড'), max_length=10,
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
        blank=False, null=True
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.bn_name
