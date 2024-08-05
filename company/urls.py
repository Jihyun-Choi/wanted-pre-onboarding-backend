from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet


app_name = "company"
router = DefaultRouter()
router.register("", CompanyViewSet)

urlpatterns = []

urlpatterns += router.urls
