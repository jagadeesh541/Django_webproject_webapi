from django.db import models

# Create your models here.


class ActivityPeriods(models.Model):
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)


class Members(models.Model):
    id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=21)
    tz = models.CharField(max_length=21)
    activity_periods = models.ForeignKey(ActivityPeriods, on_delete=models.CASCADE)

    class Meta:
        abstract = True




