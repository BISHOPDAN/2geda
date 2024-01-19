# Generated by Django 5.0.1 on 2024-01-14 11:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=100)),
                ('business_address', models.CharField(max_length=100)),
                ('business_description', models.CharField(max_length=1000)),
                ('phone_Number', models.BigIntegerField()),
                ('email_address', models.CharField(max_length=200)),
                ('website', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UploadDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_license', models.ImageField(blank=True, null=True, upload_to=None)),
                ('tax_id_number', models.CharField(max_length=100)),
                ('utility_bill', models.ImageField(blank=True, null=True, upload_to=None)),
                ('business_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='geda.businessdetails')),
            ],
        ),
        migrations.CreateModel(
            name='VerifyIdentity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone_Number', models.BigIntegerField()),
                ('email_address', models.CharField(max_length=200)),
                ('upload_document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='geda.uploaddocument')),
            ],
        ),
    ]
