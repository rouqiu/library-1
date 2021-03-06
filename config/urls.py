# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # url(r'^test-form', ),
    # Django Admin
    url(r'^admin/', include(admin.site.urls)),

    # User management
    url(r'^users/', include("books_authors.users.urls", namespace="users")),
    url(r'^accounts/', include('allauth.urls')),

    # REST Framework:
    url(r'api/', include('books_authors.api.urls', namespace="api")),
    url(r'api-auth/', include('rest_framework.urls', namespace="rest_framework")),

    url('^', include('books_authors.library.urls', namespace='library')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', 'django.views.defaults.bad_request'),
        url(r'^403/$', 'django.views.defaults.permission_denied'),
        url(r'^404/$', 'django.views.defaults.page_not_found'),
        url(r'^500/$', 'django.views.defaults.server_error'),

    ]
