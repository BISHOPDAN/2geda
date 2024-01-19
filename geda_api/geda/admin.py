from django.contrib import admin
from .models import BusinessDetails, UploadDocument, VerifyIdentity

@admin.register(BusinessDetails)
class BusinessDetailsAdmin(admin.ModelAdmin):
    list_display = ('business_name', 'business_address',
                    'phone_Number',)

admin.site.register([UploadDocument, VerifyIdentity])
