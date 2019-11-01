from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("apps.events.urls", namespace='events')),
    path('', include("apps.wallet.urls", namespace='wallet')),
]
