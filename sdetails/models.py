from django.db import models

class course(models.Model):
    name=models.CharField(max_length=10)
    discription=models.TextField(blank=True,null=True)
    def __str__(self):
        return self.name
    
class student(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.EmailField(unique=True,default='')
    courses=models.ManyToManyField(course,related_name='students',blank=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
