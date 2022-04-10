from django.db import models

# Create your models here.

class rafflePeople(models.Model):
    firstName = models.CharField(max_length=100, null=True, default='', blank=True)
    lastName = models.CharField(max_length=100, null=True, default='', blank=True)
    age=models.IntegerField(null=True, default='', blank=True)
    birthday=models.CharField(max_length=100, null=True, default='', blank=True)
    address = models.CharField(max_length=1000, null=True, default='', blank=True)
    sex=models.CharField(max_length=10, null=True, default='', blank=True)
    contactNumber=models.CharField(max_length=20, null=True, default='', blank=True)
    lokal=models.CharField(max_length=40, null=True, default='', blank=True)
    data_created=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.firstName