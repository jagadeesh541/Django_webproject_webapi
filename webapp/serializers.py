from .models import ActivityPeriods
from rest_framework import serializers


class ActivityPeriodsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriods
        fields = "__all__"
