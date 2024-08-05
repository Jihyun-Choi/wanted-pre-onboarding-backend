from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from recruitment.models import JobPosting
from user.models import User


class JobApplication(models.Model):
    """Model definition for JobApplication."""

    job_posting = models.ForeignKey(
        JobPosting,
        on_delete=models.CASCADE,
        verbose_name="채용공고_id",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="사용자_id",
    )
    applied_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="지원 일자",
    )

    class Meta:
        """Meta definition for JobApplication."""

        verbose_name = "Job Application"
        verbose_name_plural = "Job Applications"
        db_table = "job_application"
        constraints = [
            models.UniqueConstraint(
                fields=["job_posting", "user"], name="unique_job_application"
            )
        ]

    def __str__(self):
        return (
            f"[{self.id}] 사용자 {self.user.user_name} -> {self.job_posting.position}"
        )
