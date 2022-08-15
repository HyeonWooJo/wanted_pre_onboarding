from django.db import models

from postings.models import Posting

class Company(models.Model):
    name     = models.CharField(null=True, max_length=100)
    country  = models.CharField(null=True, max_length=100)
    location = models.CharField(null=True, max_length=100)
    posting  = models.ForeignKey(Posting, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'companies'