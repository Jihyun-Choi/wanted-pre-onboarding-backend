from django.db import models
from company.models import Company


class JobPosting(models.Model):
    """Model definition for JobPosting."""

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        verbose_name="회사_id",
    )
    position = models.CharField(
        default="",
        max_length=255,
        null=False,
        blank=False,
        verbose_name="채용포지션",
    )
    reward = models.BigIntegerField(
        default=0,
        verbose_name="채용보상금",
    )
    skills = models.CharField(
        default="",
        max_length=255,
        null=False,
        blank=False,
        verbose_name="사용기술",
    )
    description = models.TextField(
        default="",
        null=False,
        blank=False,
        verbose_name="채용내용",
    )

    class Meta:
        """Meta definition for JobPosting."""

        verbose_name = "Job Posting"
        verbose_name_plural = "Job Postings"
        db_table = "job_posting"

    def __str__(self):
        return f"[{self.id}] {self.company.company_name} ({self.position})"
