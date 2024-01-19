from django.shortcuts import render
from rest_framework import generics
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from .models import BusinessDetails, UploadDocument, VerifyIdentity

class CreateBusinessDetails(generics.CreateAPIView):
    """
    """
    serializer_class = serializers.BusinessDetailsSerializer

    def perform_create(self, serializer):
        serializer.save()


class ListBusinessDetails(generics.ListAPIView):
    queryset = BusinessDetails.objects.all()
    serializer_class = serializers.BusinessDetailsSerializer


class RetrieveBusinessDetails(APIView):
    def get(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(BusinessDetails, id=id)
        serializer = serializers.BusinessDetailsSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateBusinessDetails(generics.UpdateAPIView):
    queryset = BusinessDetails.objects.all()
    serializer_class = serializers.BusinessDetailsSerializer


class DeleteBusinessDetails(generics.DestroyAPIView):
    queryset = BusinessDetails.objects.all()
    serializer_class = serializers.BusinessDetailsSerializer


class CreateUploadDocument(generics.CreateAPIView):
    serializer_class = serializers.UploadDocumentSerializer

    def perform_create(self, serializer):
        serializer.save


class ListUploadDocument(APIView):
    def get(self, request, *args, **kwargs):
        queryset = UploadDocument.objects.all()
        serializer = serializers.UploadDocumentSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class RetrieveUploadDocument(APIView):
    def get(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(UploadDocument, id=id)
        serializer = serializers.UploadDocumentSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateUploadDocument(generics.UpdateAPIView):
    queryset = UploadDocument.objects.all()
    serializer_class = serializers.UploadDocumentSerializer


class DeleteUploadDocument(generics.DestroyAPIView):
    queryset = UploadDocument.objects.all()
    serializer_class = serializers.UploadDocumentSerializer


class CreateVerifyIdentity(generics.CreateAPIView):
    serializer_class = serializers.VerifyIdentitySerializer

    def perform_create(self, serializer):
        serializer.save


class ListVerifyIdentity(APIView):
    def get(self, request, *args, **kwargs):
        queryset = VerifyIdentity.objects.all()
        serializer = serializers.VerifyIdentitySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class RetrieveVerifyIdentity(APIView):
    def get(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(VerifyIdentity, id=id)
        serializer = serializers.VerifyIdentitySerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateVerifyIdentity(generics.UpdateAPIView):
    queryset = VerifyIdentity.objects.all()
    serializer_class = serializers.VerifyIdentitySerializer


class DeleteVerifyIdentity(generics.DestroyAPIView):
    queryset = VerifyIdentity.objects.all()
    serializer_class = serializers.VerifyIdentitySerializer
