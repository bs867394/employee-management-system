"""
URL configuration for emp_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='home'),
    path("view_employee", views.view_employee, name='view_employee'),
    path("add_employee", views.add_employee, name='add_employee'),
    path("delete_employee", views.delete_employee, name='delete_employee'),
    path("delete_employee/<int:emp_id>", views.delete_employee, name='delete_employee'),
    path("update_employee", views.update_employee, name='update_employee'),
]

