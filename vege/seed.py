from faker import Faker
fake=Faker()
import random
from vege.models import *
def seed_db(n=10):
    for i in range(0,n):
        departments_obj=Department.objects.all()
        random_index=random.randint(0,len(departments_obj)-1)
        student_id='UTF{}'.format(random.randint(10,1000))
        department=departments_obj[random_index]
        student_email=fake.email()
        father_email=fake.email()
        student_name=fake.name()
        student_address=fake.address()
        student_age=random.randint(20,50)
        student_id_obj=studentId.objects.create(student_id=student_id)

        x=student.objects.create(
            depatment=department,
            studentid=student_id_obj,
            student_name=student_name,
            father_email=father_email,
            student_email=student_email,
            student_age=student_age,
            student_address=student_address,
        )
def subject_marks_func(n=10):
        
        student_obj=student.objects.all()
        
        Subject_obj=Subject.objects.all()
        
        for i in student_obj:
             for j in Subject_obj:
                  y=Subject_Marks.objects.create(
                         students=i,
                         subject=j,
                         marks=random.randint(0,100)
                    )


