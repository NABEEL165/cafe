"""
URL configuration for cafe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.index, name='index'),
    # path('adminlogin', views.adminlogin, name='adminlogin'),
    # path('adminprofile', views.adminprofile, name='adminprofile'),


    path('contact/', views.contact, name='contact'),
    path('book/', views.book, name='book'),
    

    path('view/', views.view, name='view'),
   
    path('register/', views.register, name='register'),

    path('login/', views.user_login, name='login'),

    # path('usercontact/', views.contact_list, name='usercontact'),
    # path('logout/', views.user_logout, name='logout'),
    path('userbooking/', views.booking_list, name='userbooking'),
    path('usercontact/', views.contact_list, name='usercontact'),
    path('update/<int:id>/', views.update_contact, name='update_contact'),
    path('delete/<int:id>/', views.delete_contact, name='delete_contact'),
    path('booking/update/<int:id>/', views.update_booking, name='update_booking'),
    path('booking/delete/<int:id>/', views.delete_booking, name='delete_booking'),
    # path('admin/register/', views.admin_register, name='admin-register'),

    

    
    
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
