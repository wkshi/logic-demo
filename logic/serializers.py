from rest_framework import serializers
from logic.models import Logic


class LogicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logic
        fields = ('id', 'function', 'input_string', 'result')
