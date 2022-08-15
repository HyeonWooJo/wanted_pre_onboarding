from django.db import models

from postings.models import Posting

class Company(models.Model):
    position = models.CharField(null=True, max_length=100)
    reward   = models.IntegerField(default=0)
    content  = models.CharField(null=True, max_length=300)
    stack    = models.CharField(null=True, max_length=100)
    posting  = models.ForeignKey(Posting, on_delete=models.CASCADE)

    class Meta:
        db_table = 'companies'