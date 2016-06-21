from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Name(models.Model):
    name_text = models.CharField(max_length=200)
    entry_date = models.DateTimeField('date added')

    def __str__(self):
        return self.name_text
