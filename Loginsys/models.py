from django.db import models

class Newuser(models.Model):
    Username=models.CharField(max_length=150)
    Email=models.CharField(max_length=150)
    Pwd=models.CharField(max_length=150)
    Confirmpwd=models.CharField(max_length=150)
    Address=models.CharField(max_length=200)
    