from django.contrib import admin

from habit.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = (
        "action",
        "creator",
        "is_published",
    )
    list_filter = ("creator",)
    search_fields = ("action",)
