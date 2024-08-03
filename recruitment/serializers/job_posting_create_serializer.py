from rest_framework import serializers
from company.models import Company
from recruitment.models import JobPosting


class JobPostingCreateSerializer(serializers.ModelSerializer):
    """Serializer definition for JobPosting Model."""

    company_id = serializers.PrimaryKeyRelatedField(
        queryset=Company.objects.all(),
        write_only=True,
        source="company",
    )

    class Meta:
        """Meta definition for JobPostingCreateSerializer."""

        model = JobPosting
        fields = [
            "id",
            "company_id",
            "position",
            "reward",
            "skills",
            "description",
        ]
        read_only_fields = [
            "id",
            "company_id",
        ]
