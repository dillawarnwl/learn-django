from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
admin.site.site_header = ' PyBlog Admin'
admin.site.index_title = 'Customization App'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
