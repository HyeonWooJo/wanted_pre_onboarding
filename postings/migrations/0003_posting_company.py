# Generated by Django 4.1 on 2022-08-16 00:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_remove_company_posting'),
        ('postings', '0002_rename_comapny_name_posting_position_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='posting',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.company'),
        ),
    ]
