from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


admin.sites.AdminSite.site_header = 'Centre for Strategic and International Studies'
admin.sites.AdminSite.site_title = 'Centre for Strategic and International Studies'
admin.sites.AdminSite.index_title = 'Centre for Strategic and International Studies'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web.url')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)