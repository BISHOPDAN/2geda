from django.db import models

class BusinessDetails(models.Model):
    business_name = models.CharField(max_length=100)
    business_address = models.CharField(max_length=100)
    business_description = models.CharField(max_length=1000)
    phone_Number = models.BigIntegerField()
    email_address = models.CharField(max_length=200)
    website = models.URLField(blank=True)
    
    def __str__(self) -> str:
        return self.business_name
    

class UploadDocument(models.Model):
    business_license = models.ImageField(
        upload_to=None, null=True, blank=True)
    tax_id_number = models.CharField(max_length=100)
    utility_bill = models.ImageField(
        upload_to=None, null=True, blank=True)
    business_details = models.ForeignKey(BusinessDetails, 
                                         related_name="customer", on_delete=models.CASCADE)

    
    def __str__(self) -> str:
        return self.tax_id_number
    

class VerifyIdentity(models.Model):
    DOCUMENT_CHOICES = [
        ('NIN', 'National Identification Number (NIN)'),
        ('DL', "Driver's License"),
        ('VC', "Voter's Card"),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_Number = models.BigIntegerField()
    email_address = models.CharField(max_length=200)
    upload_document = models.ForeignKey(UploadDocument, 
                                         related_name="customer", 
                                         on_delete=models.CASCADE)
    document_type = models.CharField(
        max_length=3,
        choices=DOCUMENT_CHOICES,
        default='NIN',
    )


    def __str__(self) -> str:
        return self.first_name
