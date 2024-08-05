from django.urls import path
from rest_framework.routers import DefaultRouter
from recruitment.views import JobPostingViewSet, JobApplicationCreateAPIView

app_name = "recruitment"
router = DefaultRouter()
router.register(r"", JobPostingViewSet)

urlpatterns = [
    path(
        "apply/", JobApplicationCreateAPIView.as_view(), name="job-application-create"
    ),
]

urlpatterns += router.urls
