# Generated by Django 4.1 on 2022-08-15 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('postings', '0002_rename_comapny_name_posting_position_and_more'),
        ('companies', '0002_rename_position_company_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='posting',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='postings.posting'),
        ),
    ]
