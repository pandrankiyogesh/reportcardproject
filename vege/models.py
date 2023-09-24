from django.db import models
from django.contrib.auth.models import User
class Recepe(models.Model):
    #the user is the object os the User class
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    receipe=models.CharField(max_length=100)
    receipe_description=models.TextField()
    receipe_image=models.ImageField(upload_to="receipe")
    receipe_count=models.IntegerField(default=1)

class Department(models.Model):
    department=models.CharField(max_length=10,unique=True)

    def __str__(self)->str:
        return self.department
    class Meta:
        ordering = ['department']

class studentId(models.Model):
    student_id=models.CharField(max_length=10)

    def __str__(self):
        return self.student_id
    
class Subject(models.Model):
    subject_name=models.CharField(max_length=10)
    def __str__(self):
        return self.subject_name

class student(models.Model):
    depatment=models.ForeignKey(Department,related_name="depart",on_delete=models.CASCADE)
    studentid=models.OneToOneField(studentId,related_name="studentid",on_delete=models.CASCADE)
    student_email=models.EmailField(unique=True)
    father_email=models.EmailField(unique=True,default=30)
    student_name=models.CharField(max_length=10)
    student_age=models.IntegerField(default=18)
    student_address=models.TextField()

    def __str__(self):
        return self.student_name
    
    class Meta:
        ordering=['student_name']

class Subject_Marks(models.Model):
    students=models.ForeignKey(student,related_name="studentmarks",on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    marks=models.IntegerField(default=20)


    def __str__(self):
        return "{} {}".format(self.students.student_name,self.subject.subject_name) #through created objects accessing
    
    class Meta: #to avoid the data redundancy concept
         unique_together=['students','subject']
    