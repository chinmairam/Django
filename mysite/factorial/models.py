from django.db import models

# Create your models here.


class FactorialPost(models.Model):
    num = models.CharField(max_length=100)
    res = models.CharField(max_length=100)
    def __str__(self):
        return self.num + ', ' + self.res
