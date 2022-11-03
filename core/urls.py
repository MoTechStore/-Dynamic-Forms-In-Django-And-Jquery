from django.urls import path, include
from . import views


urlpatterns = [
path('', views.home, name='home'),
path('tech/', views.tech, name='tech'),
path('tech/ajax/', views.techAjax, name='techajax'),
path('motech/', views.motech, name='motech'),
path('save/', views.save_data, name='save'),
path('delete/', views.delete_data, name='delete'),
path('edit/', views.edit_data, name='edit'),
path('company/', views.Company, name='company'),
path('company/upload/', views.file_upload, name='file_upload'),




]
