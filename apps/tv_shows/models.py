from __future__ import unicode_literals
from django.db import models
from datetime import datetime

# Create your models here.
class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Network should be at least 3 characters"
        if len(postData['date']) == 10:
            input_date = datetime.strptime(postData['date'],("%Y-%m-%d"))
            if input_date > datetime.now():
                errors["date"] = "Release Date should be in the past"
        if len(postData['desc']):
            if len(postData['desc'])< 10:
                errors["desc"] = "Optional, should be at least 10 characters"
        return errors

class Shows(models.Model):
    title= models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    date = models.DateField()
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager() 

    def __repr__(self):
        return f"{self.title} {self.network} {self.date}" 
