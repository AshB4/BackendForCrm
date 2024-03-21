"""
URL configuration for be_crm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("mybe.urls")), #includes your apps URL pattern
]

# Acts as a routing mechanism for your Django project.
# Contains a mapping between URL patterns and views or viewsets.
# When a user makes a request to a specific URL, Django uses the patterns defined in urls.py to determine which view function or viewset should handle the request.
# URLs are typically defined using regular expressions (regex) patterns to match the requested URL.
# Allows you to organize your application's URLs into logical components and namespaces using include() and path() functions.
# You can also define URL parameters to capture dynamic parts of the URL and pass them as arguments to view functions.
# Supports both function-based views and class-based views.
# The urls.py file serves as a central hub for defining the URL structure of your Django project and plays a crucial role in directing incoming
# requests to the appropriate parts of your application for processing

# After you have created your project (be_crm)
# must write path from that app to urls.py here in inital folder
