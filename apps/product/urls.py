from rest_framework.routers import DefaultRouter

from apps.product.views import ProductAPIViewSet, ProductImageAPIViewSet
from apps.order.views import AddressApiViewSet


router = DefaultRouter()
router.register('products', ProductAPIViewSet)
router.register('images', ProductImageAPIViewSet)
router.register('address', AddressApiViewSet    )


urlpatterns = router.urls