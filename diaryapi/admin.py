from django.contrib import admin

from .models import DiaryPost


@admin.register(DiaryPost)
class TodoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'timestamp',
        'post'
    )
