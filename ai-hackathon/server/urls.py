from rest_framework import routers
from django.urls import path, include
from .api import UserViewSet, ChartsView

router = routers.DefaultRouter()
router.register("api/user", UserViewSet, "user")
# router.register("api/charts/<int:pk>", ChartsView.as_view(), "charts")

# urlpatterns = router.urls

urlpatterns = [
    path("api/charts/<int:pk>", ChartsView.as_view(), "charts"),
    path("", include(router.urls))
]
