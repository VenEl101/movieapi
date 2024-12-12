
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny
from drf_yasg import openapi

schema_view = get_schema_view(

    openapi.Info(
        title="Music Application Rest API",
        default_version="v1",
        description="Swagger docs for REST API",
        contact=openapi.Contact("Ve 001 <gmail@1234qwert.com"),
    ),

    public=True,
    permission_classes=(AllowAny,)
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('movies.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-docs'),
]


