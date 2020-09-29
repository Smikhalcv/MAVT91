"""mavt91 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings

from app.views import input_coordinate_db, mapping, show_coordinates, base

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mapping/', mapping, name='mapping'),
    path('show_coordinates/', show_coordinates, name='show_coordinates'),
    path('get_coordinate/', input_coordinate_db, name='input_coordinate_db'),
    path('', base, name='base')
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
       path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
