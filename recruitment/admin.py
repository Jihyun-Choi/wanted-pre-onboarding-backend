from django.contrib import admin
from recruitment.models import JobPosting


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
