from django.db import models

from companies.models import Company

class Posting(models.Model):
    position = models.CharField(null=True, max_length=100)
    reward   = models.IntegerField(default=0)
    content  = models.CharField(null=True, max_length=300)
    stack    = models.CharField(null=True, max_length=100)
    company  = models.ForeignKey(Company, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'postings'