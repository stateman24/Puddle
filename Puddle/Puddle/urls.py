from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include




urlpatterns = [
    path("", include('core.urls', namespace='core')),
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path("items/", include('Item.urls', namespace='item')),
    path('Dashboard/', include('Dashboard.urls', namespace='Dashboard')),
    path('Inbox/', include('conversation.urls', namespace='conversation')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
