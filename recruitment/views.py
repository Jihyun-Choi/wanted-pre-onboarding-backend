from rest_framework import viewsets
from recruitment.models import JobPosting
from recruitment.serializers import (
    JobPostingCreateSerializer,
    JobPostingUpdateSerializer,
    JobPostingSerializer,
    JobPostingDetailSerializer,
)


class JobPostingViewSet(viewsets.ModelViewSet):
    queryset = JobPosting.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return JobPostingCreateSerializer
        elif self.action in ["update", "partial_update"]:
            return JobPostingUpdateSerializer
        elif self.action == "list":
            return JobPostingSerializer
        elif self.action == "retrieve":
            return JobPostingDetailSerializer
        return JobPostingDetailSerializer
