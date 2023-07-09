from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Projectblog List API",
        default_version='v1',
        description="Books library project",
        terms_of_service="demo.com",
        contact=openapi.Contact(email="abdusalomovshaxobiddin5@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('account/', include('django.contrib.auth.urls')),
    path('account/', include('accounts.urls')),
    path('', include('blog.urls')),

    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),

    path('api/v1/dj-rest-auth/registration', include('dj_rest_auth.registration.urls')),
    path('api/allauth/', include('allauth.urls')),
    path('api/v1/', include('api.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
