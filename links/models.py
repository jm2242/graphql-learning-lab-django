from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Link(models.Model):
    url = models.URLField()
    description = models.TextField(null=True, blank=True)


class Vote(models.Model):
    link = models.ForeignKey('links.Link', related_name='votes', on_delete=models.deletion.CASCADE)