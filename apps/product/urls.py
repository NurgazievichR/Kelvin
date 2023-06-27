from rest_framework.routers import DefaultRouter

from apps.product.views import ProductAPIViewSet, ProductImageAPIViewSet


router = DefaultRouter()
router.register('products', ProductAPIViewSet)
router.register('images', ProductImageAPIViewSet)


urlpatterns = router.urls