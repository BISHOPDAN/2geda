from django.urls import path, include
from . import views

urlpatterns = [
    path('create/business/detail/', 
         views.CreateBusinessDetails.as_view(), name='business'),
    
    path('list/business/detail/',
         views.ListBusinessDetails.as_view(), name='business'),

    path('retrieve/business/detail/<int:pk>/', 
         views.RetrieveBusinessDetails.as_view(), name='business'),

    path('update/business/detail/<int:pk>/', 
         views.UpdateBusinessDetails.as_view(), name='business'),

    path('delete/business/detail/<int:pk>/', 
         views.DeleteBusinessDetails.as_view(), name='business'),
    
    path('create/upload/document',
         views.CreateUploadDocument.as_view(), name='upload'),

    path('list/upload/document/', 
         views.ListUploadDocument.as_view(), name='upload'),

    path('retrieve/upload/document/<int:pk>/', 
         views.RetrieveUploadDocument.as_view(), name='upload'),


    path('update/upload/document/<int:pk>/', 
         views.UpdateUploadDocument.as_view(), name='upload'),


    path('delete/upload/document/<int:pk>/', 
         views.DeleteBusinessDetails.as_view(), name='upload'),
    

    path('create/verify/', 
         views.CreateVerifyIdentity.as_view(), name='verify'),

    path('list/verify/', 
         views.ListVerifyIdentity.as_view(), name='verify'),
    

    path('retrieve/verify/<int:pk>/', 
         views.RetrieveVerifyIdentity.as_view(), name='upload'),

    path('update/verify/<int:pk>/', 
         views.UpdateVerifyIdentity.as_view(), name='upload'),


    path('delete/verify/<int:pk>/', 
         views.DeleteVerifyIdentity.as_view(), name='upload'),
]
