from django.db import models


class Expenses(models.Model):
    id       = models.AutoField(primary_key=True)
    amount   = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date     = models.DateField()
    account  = models.CharField(max_length=100)
    note     = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)

class Accounts(models.Model):
    id           = models.AutoField(primary_key=True)
    name         = models.CharField(max_length=100)
    balance      = models.DecimalField(max_digits=10, decimal_places=2)
    note         = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)