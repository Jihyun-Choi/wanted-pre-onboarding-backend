from django.urls import path, include
from rest_framework.routers import DefaultRouter
from recruitment.views import JobPostingViewSet


app_name = "recruitment"
router = DefaultRouter()
router.register(r"", JobPostingViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path(
        "apply/", JobApplicationCreateAPIView.as_view(), name="job-application-create"
    ),
]
