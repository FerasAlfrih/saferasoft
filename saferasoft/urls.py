"""saferasoft URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views as mv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', mv.about, name="about"),
    path('profolio/', mv.profolio, name="profolio"),
    path('team/', mv.team, name="team"),
    path('contact/', mv.contact, name="contact"),
    path('services/', mv.services, name="services"),
    path('cov19/', include('covid19.urls')),
    path('', include('base.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
