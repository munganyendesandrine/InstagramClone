"""instagram_clone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^',include('instagram_cloneapp.urls',namespace="instagram_cloneapp")),
    url(r'',include('instagram_cloneapp.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^logout', views.logout, {"next_page": '/'}), 
]

# 1

# Here is the issue:

# url(r'^$', include('app.urls')),
# Should be

# url(r'^', include('app.urls', namespace="app")),