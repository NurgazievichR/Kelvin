from rest_framework.routers import DefaultRouter

from apps.order.views import OrderApiViewSet

router = DefaultRouter()
router.register('', OrderApiViewSet)


urlpatterns = router.urls

