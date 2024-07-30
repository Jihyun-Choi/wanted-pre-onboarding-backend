from django.db import models


class User(models.Model):
    """Model definition for User."""

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    user_name = models.CharField(max_length=255)
    email = models.EmailField()

    class Meta:
        """Meta definition for Company."""

        verbose_name = "Company"
        verbose_name_plural = "Companies"
        db_table = "company"

    def __str__(self) -> str:
        return f"[{self.id}] {self.user_name} ({self.email})"
