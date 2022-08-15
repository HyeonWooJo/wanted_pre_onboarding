from django.db import models

class User(models.Model):
    name          = models.CharField(max_length=60)
    email         = models.CharField(max_length=150, unique=True)
    password      = models.CharField(max_length=200)
    nickname      = models.CharField(max_length=50, unique=True)
    address       = models.CharField(max_length=50, null=True)
    mobile_number = models.CharField(max_length=50, null=True)
    
    class Meta:
        db_table = "users"