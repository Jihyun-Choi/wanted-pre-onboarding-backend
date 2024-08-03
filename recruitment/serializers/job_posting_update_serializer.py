from rest_framework import serializers
from recruitment.models import JobPosting


class JobPostingUpdateSerializer(serializers.ModelSerializer):
    """Serializer definition for JobPosting Model."""

    class Meta:
        """Meta definition for JobPostingUpdateSerializer."""

        model = JobPosting
        fields = [
            "id",
            "position",
            "reward",
            "skills",
            "description",
        ]
        read_only_fields = [
            "id",
        ]

    def update(self, instance, validated_data):
        validated_data.pop("company", None)
        return super().update(instance, validated_data)
