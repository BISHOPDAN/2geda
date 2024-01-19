# Generated by Django 5.0.1 on 2024-01-19 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='verifyidentity',
            name='document_type',
            field=models.CharField(choices=[('NIN', 'National Identification Number (NIN)'), ('DL', "Driver's License"), ('VC', "Voter's Card")], default='NIN', max_length=3),
        ),
    ]
