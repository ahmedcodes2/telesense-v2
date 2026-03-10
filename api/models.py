import uuid

from django.db import models

class Organisation(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    name = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'organisations'

class Sensor(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    organisation = models.ForeignKey(
        Organisation,
        on_delete=models.CASCADE,
        db_column='org_id',
        related_name='sensors'
    )
    serial_number = models.TextField(unique=True)
    model = models.TextField()
    firmware_version = models.TextField(null=True, blank=True)
    installed_at = models.DateTimeField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'sensors'
        indexes = [
            models.Index(fields=['organisation'], name='idx_sensors_org'),
        ]

class Telemetry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    time = models.DateTimeField(auto_now_add=True)
    sensor = models.ForeignKey(
        Sensor,
        on_delete=models.CASCADE,
        db_column='sensor_id',
        related_name='telemetry'
    )
    organisation = models.ForeignKey(
        Organisation,
        on_delete=models.CASCADE,
        db_column='org_id',
    )
    temperature = models.FloatField(null=True, blank=True)
    humidity = models.FloatField(null=True, blank=True)
    co2_ppm = models.FloatField(null=True, blank=True)
    pm25 = models.FloatField(null=True, blank=True)
    noise_db = models.FloatField(null=True, blank=True)
    battery_voltage = models.FloatField(null=True, blank=True)
    cpu_temp = models.FloatField(null=True, blank=True)

    signal_strength = models.IntegerField(null=True, blank=True)

    status = models.TextField(null=True, blank=True)
    firmware_version = models.TextField(null=True, blank=True)

    raw_payload = models.JSONField(null=True, blank=True)

    class Meta:
        db_table = 'telemetry'
        # managed = False # IMPORTANT FOR HYPERTABLE SINCE I AM NOT MANAGING IT
        constraints = [
            models.UniqueConstraint(
                fields=['time', 'sensor'],
                name='telemetry_unique_time_sensor'
            )
        ]
        indexes = [
            models.Index(fields=['-time'], name='idx_telemetry_time'),
            models.Index(fields=['sensor', '-time'], name='idx_telemetry_sensor_time'),
            models.Index(fields=['organisation', '-time'], name='idx_telemetry_org_time'),
        ]