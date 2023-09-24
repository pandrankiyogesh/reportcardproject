from django.db import models


#structure of schema wiill be written

class Student(models.Model):
    name=models.CharField(max_length=18)
    age=models.IntegerField()
    email=models.EmailField()
    address=models.TextField(null=True,blank=True)

#CRUD operations
#Car.objects.create() demooo
#create()-creating
#get()-accessing the data
#Update-updating the data
#Delete-deleting the data


class Car(models.Model):
    #these are the instance variables.
    car_name=models.CharField(max_length=500)
    speed=models.IntegerField(default=50)

    def __str__(self):
        return self.car_name
