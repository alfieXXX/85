from django.db import models

# Create your models here.
class raf(models.Model):
    fName = models.CharField(max_length=100, null=True, default='', blank=True)
    lName = models.CharField(max_length=100, null=True, default='', blank=True)
    lokal=models.CharField(max_length=40, null=True, default='', blank=True)
    data_created=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fName