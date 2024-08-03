from rest_framework import serializers
from company.models import Company


class CompanySerializer(serializers.ModelSerializer):
    """Serializer definition for Company Model."""

    class Meta:
        """Meta definition for CompanySerializer."""

        model = Company
        fields = [
            "id",
            "company_name",
            "country",
            "region",
        ]
