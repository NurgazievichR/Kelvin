from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.promocode.views import PromocodeViewSet


router = DefaultRouter()
router.register('', PromocodeViewSet)


urlpatterns = router.urls
