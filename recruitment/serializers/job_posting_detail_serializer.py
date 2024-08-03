from rest_framework import serializers
from recruitment.models import JobPosting
from recruitment.serializers import JobPostingSerializer


class JobPostingDetailSerializer(JobPostingSerializer):
    """Serializer definition for JobPosting Model."""

    other_job_postings = serializers.SerializerMethodField()

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
            "other_job_postings",
        ]
        read_only_fields = [
            "id",
            "company_name",
            "country",
            "region",
            "other_job_postings",
        ]

    def get_other_job_postings(self, obj):
        return (
            JobPosting.objects.filter(company=obj.company)
            .exclude(id=obj.id)
            .values_list("id", flat=True)
        )
