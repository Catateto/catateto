from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


class RealEstate(models.Model):
    url = models.URLField(unique=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Real estate')
        verbose_name_plural = _('Real estates')

    def __unicode__(self):
        return self.url


class Immobile(models.Model):
    OBJECTIVE_CHOICES = [
        ('for_sale', _('For Sale')),
        ('for_rent', _('For Rent'))
    ]

    realestate = models.ForeignKey(RealEstate)
    url = models.URLField(unique=True)

    title = models.CharField(_('Title'), max_length=255)
    subtitle = models.CharField(_('Subtitle'), max_length=255)

    price = models.DecimalField(_('Price'), max_digits=12, decimal_places=2)
    objective = models.CharField(
        _('Objective'), max_length=30, choices=OBJECTIVE_CHOICES)
    property_type = models.CharField(_('Property Type'), max_length=255)
    bedroms = models.PositiveSmallIntegerField(_('Bedrooms'), default=0)
    bathroms = models.PositiveSmallIntegerField(_('Bathrooms'), default=0)
    parking = models.PositiveSmallIntegerField(_('Parking'), default=0)

    # address
    city = models.CharField(_('City'), max_length=75)
    state = models.CharField(_('State'), max_length=2)
    neighborhood = models.CharField(
        _('Neighborhood'), max_length=75, blank=True)
    street = models.CharField(_('Street'), max_length=75, blank=True)
    lon = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Immobile')
        verbose_name_plural = _('Immobiles')

    def __unicode__(self):
        return self.url


class Image(models.Model):
    url = models.URLField(unique=True)
    immobile = models.ForeignKey(Immobile)

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')
