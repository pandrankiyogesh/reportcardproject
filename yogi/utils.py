from yogi.models import Student
import time
student=Student(3,'ramu',24,"ramu@gmail.com","vizag")
student.save()
def run():
    print("function started")
    time.sleep(1)
    print("function ended")


