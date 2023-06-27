from rest_framework.routers import DefaultRouter

from apps.product.views import ProductAPIViewSet, ProductImageAPIViewSet


router = DefaultRouter()
router.register('', ProductAPIViewSet)
router.register('images/', ProductImageAPIViewSet)