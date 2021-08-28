from django.db import models
from jsonfield import JSONField


# Create your models here.
class ESPObject(models.Model):
    unique_id = models.IntegerField(unique=True, max_length=11)
    last_location_time = models.DateTimeField(null=True,blank=True)
    user_name = models.CharField(max_length=64)
    user_roll_no = models.IntegerField(max_length=11)
    last_ips = JSONField(null=True,blank=True)
