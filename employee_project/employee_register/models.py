from django.db import models
from django.db.models.deletion import CASCADE

class Position(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Employee(models.Model):
    fullname = models.CharField(max_length = 100)
    emp_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length=15)
    position = models.CharField(max_length=100)
    title = models.ForeignKey(Position, on_delete = CASCADE)

    def __str__(self):
        return self.fullname

 