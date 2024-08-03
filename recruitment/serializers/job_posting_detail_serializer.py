from recruitment.models import JobPosting
from recruitment.serializers import JobPostingSerializer


class JobPostingDetailSerializer(JobPostingSerializer):
    """Serializer definition for JobPosting Model."""

    class Meta:
        """Meta definition for JobPostingDetailSerializer."""

        model = JobPosting
        fields = [
            "id",
            "company_name",
            "country",
            "region",
            "position",
            "reward",
            "skills",
            "description",
        ]
        read_only_fields = [
            "id",
            "company_name",
            "country",
            "region",
        ]
