"""geoCodeBD_app > models > abstract.py"""
# DJANGO IMPORTS
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class CommonFieldModel(models.Model):
    """Common fields abstract model """
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT,
        blank=True, null=True
    )
    is_active = models.BooleanField(
        _('Is Active'), default=True
    )
    created_at = models.DateTimeField(
        _('Created At'), auto_now_add=True, null=True
    )
    last_updated = models.DateTimeField(
        _('Last Updated'), auto_now=True, null=True
    )

    class Meta:
        abstract = True
