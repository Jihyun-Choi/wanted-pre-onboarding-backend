from django.contrib import admin
from recruitment.models import JobPosting, JobApplication


@admin.register(JobPosting)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "company",
        "position",
        "reward",
        "skills",
        "description",
    )
    search_fields = (
        "company",
        "position",
        "reward",
        "skills",
    )


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "job_posting",
        "user",
        "applied_at",
    )
    search_fields = (
        "job_posting__position",
        "user__user_name",
    )
