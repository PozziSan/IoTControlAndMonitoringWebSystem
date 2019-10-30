from django.db import models
from datetime import datetime


class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def delete(self):
        self.deleted_at = datetime.now()
        self.save()


class TemperatureMeasures(BaseModel):
    measure = models.DecimalField(decimal_places=3, max_digits=7)


class DeviceActivationLog(BaseModel):
    device = models.CharField(max_length=255)
