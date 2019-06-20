from django.db import models

# Create your models here.

class Shows(models.Model):
    title= models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    date = models.DateField()
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"{self.title} {self.network} {self.date}" 
