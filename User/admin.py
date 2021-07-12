from django.contrib import admin
from .models import blog
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
admin.site.register(blog,ProfileAdmin)
