from django.db import models

class Leki(models.Model):
    mnn = models.CharField(max_length=80, blank=True)
    torgName = models.CharField(max_length=100)
    lekForm = models.CharField(max_length=250, blank=True)
    factory = models.CharField(max_length=250, blank=True)
    ATX = models.CharField(max_length=20, blank=True)
    count = models.CharField(max_length=20, blank=True)
    predCena = models.CharField(max_length=50)
    CenaPervUpak = models.CharField(max_length=50, blank=True)
    ru = models.CharField(max_length=30,blank=True)
    dateReg = models.CharField(max_length=80, blank=True)
    EAN13 = models.CharField(max_length=20, blank=True)



    def __str__(self):
        return self.torgName

