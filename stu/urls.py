"""
URL configuration for stu project.

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

from stuuu.views import success, register_student, student_detail, student_list, admin_login

urlpatterns = [
    path('', register_student, name='register'),
    path('admin/', admin.site.urls),
    path('register/', register_student, name='register'),
    path('success/', success, name='success'),
    path('student/<int:pk>/', student_detail, name='student_detail'),
    path('students/', student_list, name='student_list'),
    path('admin-login/', admin_login, name='admin_login'),




]
