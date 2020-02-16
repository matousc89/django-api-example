from django.db import models

# Create your models here.


class Measurement(models.Model):

    value = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.value)