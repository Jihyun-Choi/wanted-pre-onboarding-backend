from django.db import models


class Company(models.Model):
    """Model definition for Company."""

    company_name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    region = models.CharField(max_length=255)

    class Meta:
        """Meta definition for Company."""

        verbose_name = "Company"
        verbose_name_plural = "Companies"
        db_table = "company"

    def __str__(self):
        return self.company_name
