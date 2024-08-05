from rest_framework import viewsets, filters
from recruitment.models import JobPosting
from recruitment.serializers import (
    JobPostingCreateSerializer,
    JobPostingUpdateSerializer,
    JobPostingSerializer,
    JobPostingDetailSerializer,
)


class JobPostingViewSet(viewsets.ModelViewSet):
    queryset = JobPosting.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = [
        "company_id__company_name",
        "company_id__country",
        "company_id__region",
        "position",
        "skills",
    ]

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
