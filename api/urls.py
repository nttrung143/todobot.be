from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from drf_yasg.generators import OpenAPISchemaGenerator


class BothHttpAndHttpsSchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.schemes = ["https", "http"]
        return schema


schema_view = get_schema_view(
    openapi.Info(
        title="Beta Webapp API",
        default_version='v1',
        description="Beta Webapp API"
    ),
    public=True,
    generator_class=BothHttpAndHttpsSchemaGenerator,  # Here
    permission_classes=[permissions.AllowAny],
    authentication_classes=[]
)

urlpatterns = [
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
]
