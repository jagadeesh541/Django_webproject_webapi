from django.shortcuts import render
from .models import ActivityPeriods
from .serializers import ActivityPeriodsSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime

'''x = datetime.now()
data = x.strftime("%b %d %Y")
data = ActivityPeriods.objects.create(start_time=data)
data.save()'''


class ActivityPeriodsListView(APIView):
    def get(self, request):
        user = ActivityPeriods.objects.all()
        serial = ActivityPeriodsSerializers(user, many=True)
        return Response(serial.data)



