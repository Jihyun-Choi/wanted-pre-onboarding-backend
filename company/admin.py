from django.contrib import admin
from .models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "company_name",
        "country",
        "region",
    )
    search_fields = (
        "company_name",
        "country",
        "region",
    )
    list_filter = (
        "country",
        "region",
    )
    ordering = ("company_name",)
