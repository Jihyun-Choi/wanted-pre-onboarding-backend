from rest_framework import serializers
from recruitment.models import JobPosting


class JobPostingSerializer(serializers.ModelSerializer):
    """Serializer definition for JobPosting Model."""

    company_name = serializers.CharField(
        source="company.company_name",
        read_only=True,
    )
    country = serializers.CharField(
        source="company.country",
        read_only=True,
    )
    region = serializers.CharField(
        source="company.region",
        read_only=True,
    )

    class Meta:
        """Meta definition for JobPostingSerializer."""

        model = JobPosting
        fields = [
            "id",
            "company_name",
            "country",
            "region",
            "position",
            "reward",
            "skills",
        ]
        read_only_fields = [
            "id",
            "company_name",
            "country",
            "region",
        ]
