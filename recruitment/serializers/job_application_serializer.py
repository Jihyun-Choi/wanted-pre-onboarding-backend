from rest_framework import serializers
from recruitment.models import JobApplication


class JobApplicationSerializer(serializers.ModelSerializer):
    """Serializer definition for JobApplication Model."""

    class Meta:
        """Meta definition for JobApplicationSerializer."""

        model = JobApplication
        fields = [
            "job_posting",
            "user",
            "applied_at",
        ]
        read_only_fields = [
            "applied_at",
        ]

    def validate(self, data):
        job_posting = data.get("job_posting")
        user = data.get("user")

        if JobApplication.objects.filter(job_posting=job_posting, user=user).exists():
            raise serializers.ValidationError(
                {"detail": "이미 해당 채용공고에 지원하셨습니다."}
            )
        return data
