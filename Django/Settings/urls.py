"""kotoko_express_dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # Django Admin
    path('dashboard/', admin.site.urls),

    # User management

    # Third-party apps
    path('django-rq/', include('django_rq.urls'))

    # Local Apps
]

# Serve Static and Media in development mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Admin page Settings
admin.site.site_header = "Kotoko Portal Admin"
admin.site.site_title = "Kotoko Portal Admin"
admin.site.index_title = "Welcome to Kotoko Portal Admin"

# Override default error pages
handler404 = 'errors.views.page_not_found_views.page_not_found'
handler500 = 'errors.views.server_error_views.server_error'
handler403 = 'errors.views.permission_denied_views.permission_denied'

