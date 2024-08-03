from rest_framework import serializers
from rest_framework.serializers import ValidationError

import habit


class HabitsValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value["is_good"]:
            if value["related"] or value["prize"]:
                raise serializers.ValidationError(
                    "У приятной привычки не может быть связанной привычки или вознаграждения"
                )
            if value["related"] and value["prize"]:
                raise serializers.ValidationError(
                    "Может быть связанная привычка или вознаграждение,"
                )
            if value["duration"] > 2:
                raise serializers.ValidationError(
                    "Длительность привычки не может быть больше 2 минут"
                )
            if value["related"]:
                if not value["related"].is_good:
                    raise serializers.ValidationError(
                        "Связанные привычки = приятные привычки"
                    )
            if value["is_good"]:
                number_list = [1, 2, 3, 4, 5, 6, 7]
                # if habit.get("number_of_executions")  not in number_list:  # > 7 or habit.get("number_of_executions") < 1:
                #     raise ValidationError("Привычку нельзя выполнять реже 1 и чаще 7 раз в неделю")
                num = habit.get("number_of_executions")
                try:
                    num in number_list
                except ValidationError:
                    print("Привычку нельзя выполнять реже 1 и чаще 7 раз в неделю")
