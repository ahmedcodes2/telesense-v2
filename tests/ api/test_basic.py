import pytest
from rest_framework.test import APIClient

from api.models import Telemetry


@pytest.fixture
def client():
    return APIClient()

@pytest.mark.django_db
def test_create_telemetry(client, sensor):
    payload = {
  "sensor": sensor.id,
  "temperature": 22.7,
  "humidity": 48.3,
  "co2_ppm": 615,
  "pm25": 12.4,
  "noise_db": 41.2,
  "battery_voltage": 3.78,
  "cpu_temp": 54.1,
  "signal_strength": -68,
  "status": "OK",
  "firmware_version": "1.2.5",
  "raw_payload": {
    "adc_raw": 3821,
    "uptime_seconds": 86400,
    "error_flags": []
  }
}

    response = client.post("/api/telemetry/", payload, format="json")

    assert response.status_code == 201
    assert Telemetry.objects.count() == 1