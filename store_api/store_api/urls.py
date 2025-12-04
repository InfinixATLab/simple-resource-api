from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import CategoryViewSet, ProductViewSet
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView



router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
  path('admin/', admin.site.urls),
  path('api/', include(router.urls)),
  path('schema/', SpectacularAPIView.as_view(), name='schema'),
  path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
]
