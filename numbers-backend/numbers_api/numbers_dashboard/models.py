from django.db import models

# Create your models here.


class NumberM(models.Model):
    name=models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    min_len=models.SmallIntegerField(default=1)
    url_end_point=models.CharField(max_length=100)
    is_serie=models.BooleanField(default=False)
    enable=models.BooleanField(default=False)


    def __str__(self):
        return self.name
