import pytest

from api.models import Organisation, Sensor


@pytest.fixture
def organisation():
    return Organisation.objects.create(name="Test Organisation")

@pytest.fixture
def sensor(organisation):
    return Sensor.objects.create(organisation=organisation, serial_number="1234567890")