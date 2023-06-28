from django.urls import path
from apps.promocode.views import PromocodeView

urlpatterns = [
    path('promocodes/', PromocodeView.as_view()),
    path('promocodes/<int:pk>', PromocodeView.as_view())
]