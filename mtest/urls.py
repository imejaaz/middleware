from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('verse/', include('verse.urls')),
    path('cookie/', include('cookie.urls')),
    path('session/', include('session.urls')),
    path('', include('test_cookie.urls')),
]
