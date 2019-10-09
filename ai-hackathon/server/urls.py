from rest_framework import routers
from django.urls import path, include
from .api import UserViewSet, ChartsView

router = routers.DefaultRouter()
router.register("api/user", UserViewSet, "user")
#router.register("api/charts/user", ChartsView.as_view(), "charts")


urlpatterns = router.urls
