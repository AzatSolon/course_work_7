from django.db import models
from datetime import timedelta
from config.settings import AUTH_USER_MODEL

NULLABLE = {"blank": True, "null": True}


class Habit(models.Model):

    creator = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Создатель", **NULLABLE
    )
    place = models.CharField(
        max_length=100, verbose_name="Место выполнения", **NULLABLE
    )
    time = models.TimeField(verbose_name="Время выполнения", **NULLABLE)
    action = models.CharField(max_length=100, verbose_name="Действие")
    habit_is_pleasant = models.BooleanField(
        default=True, verbose_name="Признак приятной привычки"
    )
    connection_habit = models.ForeignKey(
        "self", on_delete=models.CASCADE, verbose_name="Связанная привычка", **NULLABLE
    )
    number_of_executions = models.IntegerField(
        default=1, verbose_name="Количество выполнений в неделю"
    )
    duration = models.DurationField(
        default=timedelta(seconds=120), verbose_name="Продолжительность выполнения"
    )
    is_published = models.BooleanField(default=True, verbose_name="Признак публичности")
    reward = models.CharField(max_length=100, verbose_name="Вознаграждение", **NULLABLE)

    def __str__(self):
        return f"Действие: {self.action}--время:{self.time}--место:{self.place}\n(создатель {self.creator})"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
