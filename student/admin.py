from django.contrib import admin
from . import models

@admin.register(models.Profile)
class UniversityAdmin(admin.ModelAdmin):
    pass
