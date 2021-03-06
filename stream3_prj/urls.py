"""stream3_prj URL Configuration

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
from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from home import views as home_views
from donations import views as donation_views
from .settings import MEDIA_ROOT
from django.views.static import serve

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
    url(r'^$', home_views.get_index, name="index"),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^forum/', include('forum.urls')),
    url(r'^contact/', include('contact_form.urls')),
    
    # Flatpages
    url(r'^pages/', include('django.contrib.flatpages.urls')),

    # Images
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

    # Donations
    url(r'^donations/$', donation_views.donation, name='donate'),
]

# Django-Debug-Toolbar
if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(url(r'^debug/', include(debug_toolbar.urls)))
