from django.db import models


class User(models.Model):
    """Model definition for User."""

    user_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    class Meta:
        """Meta definition for User."""

        verbose_name = "User"
        verbose_name_plural = "Users"
        db_table = "user"

    def __str__(self) -> str:
        return f"[{self.id}] {self.user_name} ({self.email})"
