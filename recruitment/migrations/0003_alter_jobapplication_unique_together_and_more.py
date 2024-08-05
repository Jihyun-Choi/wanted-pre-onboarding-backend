# Generated by Django 5.0.7 on 2024-08-05 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recruitment", "0002_jobapplication"),
        ("user", "0002_alter_user_email"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="jobapplication",
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name="jobapplication",
            constraint=models.UniqueConstraint(
                fields=("job_posting", "user"), name="unique_job_application"
            ),
        ),
    ]
