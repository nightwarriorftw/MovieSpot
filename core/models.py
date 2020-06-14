import time

from django.db import models
from django.db.models import Q

from partial_date import PartialDateField

class MovieManager(models.Manager):

    def search(self, query):
        lookups = Q(title__icontains=query) | \
        Q(release_year__icontains=query) | \
        Q(location__icontains=query) | \
        Q(productionCompany__icontains=query) | \
        Q(director__icontains=query) | \
        Q(actor1__icontains=query) | \
        Q(actor2__icontains=query) | \
        Q(actor3__icontains=query)
            
        return self.filter(lookups).distinct()


class MovieSpotModel(models.Model):
    title = models.CharField(max_length=100)
    release_year = PartialDateField()
    location = models.CharField(max_length=300)
    funfacts = models.CharField(max_length=500, null=True, blank=True)
    productionCompany = models.CharField(max_length=50)
    director = models.CharField(max_length=60)
    writer = models.CharField(max_length=60)
    actor1 = models.CharField(max_length=60)
    actor2 = models.CharField(max_length=60, null=True, blank=True)
    actor3 = models.CharField(max_length=60, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = MovieManager()

    class Meta:
        ordering = ('release_year',)


    def __str__(self):
        return self.title
