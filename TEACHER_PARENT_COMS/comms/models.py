from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    CHOICES = [
        ('admin', 'ADMIN'),
        ('parent', 'PARENT'),
        ('teacher', 'TEACHER')
    ]
    role = models.CharField(choices=CHOICES, default='admin', max_length=10)


class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    tsc_no = models.CharField(max_length=20)

class Parent(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=30)
    
class events(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(blank=True,null=True,upload_to="events")
    details=models.TextField()
    def __str__(self):
        return self.title
class Session(models.Model):
    year = models.CharField(max_length=10)
    def __str__(self):
        return self.year  
class Subject(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    student_class = models.ForeignKey('StudentClass', on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.name} {self.session}'     
class Assignments(models.Model):
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    content=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.subject

class Conferencing(models.Model):
    name=models.CharField(max_length=100)
    link=models.URLField()
    date=models.DateField()
    time=models.TimeField()
    created=models.DateTimeField(auto_now_add=True)
    def  __str__(self):
        return self.name



class Student(models.Model):
    student_name = models.CharField(max_length=100)
    admission_no = models.CharField(max_length=30)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    student_class = models.ForeignKey('StudentClass', on_delete=models.CASCADE)
    def __str__(self):
        return self.student_name
        
class Studentprofile(models.Model):
    student_name = models.ForeignKey(Student,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='profile',blank=False,null='False')
    discipline= models.CharField(max_length=100)
    actions=models.TextField()
    achievement= models.CharField(max_length=100)
    def __str__(self):
        return self.action
    
class StudentClass(models.Model):
    class_name = models.CharField(max_length=50)
    def __str__(self):
        return self.class_name

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField()
    grade = models.CharField(max_length=2)

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    is_present = models.BooleanField(default=True)
