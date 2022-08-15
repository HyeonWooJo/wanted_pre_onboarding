from django.db import models

class Posting(models.Model):
    comapny_name = models.CharField(null=True, max_length=100)
    country      = models.CharField(null=True, max_length=100)
    location     = models.CharField(null=True, max_length=100)

    class Meta:
        db_table = 'postings'