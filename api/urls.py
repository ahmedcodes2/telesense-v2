from django.contrib import admin
from django.urls import path
from .views import hello, TelemetryCreateView

urlpatterns = [
    path('', hello),
    path('telemetry/', TelemetryCreateView.as_view(), name='create-telemetry')
]
