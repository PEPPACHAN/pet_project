from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
       openapi.Info(
           title="API for authorization users",
           default_version='v1',
           description="API return 2 fields 'username' and 'password'. They get 30 and 255 symbols",
           terms_of_service="---",
           contact=openapi.Contact(email="1abiturient1@gmail.com"),
           license=openapi.License(name="Open API and you can use it anywhere, if you found it"),
       ),
       public=True,
       permission_classes=(permissions.AllowAny,),
   )

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("registration.urls")),
    path("", include("product_sell.urls")),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
