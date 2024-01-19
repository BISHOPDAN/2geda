from rest_framework import serializers
from .models import BusinessDetails, UploadDocument, VerifyIdentity


class BusinessDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessDetails
        fields = ('id', 'business_name', 'business_address', 
                  'business_description', 'phone_Number', 
                  'email_address', 'website')


class UploadDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadDocument
        fields = '__all__'


class VerifyIdentitySerializer(serializers.ModelSerializer):
    class Meta:
        model = VerifyIdentity
        fields = '__all__'
