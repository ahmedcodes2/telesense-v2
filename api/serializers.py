from rest_framework import serializers
from .models import Telemetry

class TelemetrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Telemetry
        exclude = ['organisation']

    def create(self, validated_data):
        sensor = validated_data['sensor']
        validated_data['organisation'] = sensor.organisation
        return Telemetry.objects.create(**validated_data)