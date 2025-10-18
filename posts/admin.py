from django.contrib import admin

from .models import BasicPost
# Register your models here.
@admin.register(BasicPost)
class PostAdmin(admin.ModelAdmin):
    pass