from django.db import models

# Create your models here.

class EmployeeRecord(models.Model):

    eno = models.IntegerField()
    ename = models.CharField(max_length=64)
    esal = models.IntegerField()
    eaddr = models.CharField(max_length=64)


    def __str__(self):

        return self.ename#,self.eno,self.esal,self.eaddr,
