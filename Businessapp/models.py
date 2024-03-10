from django.db import models



# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)

    def __str__(self):
       return self.firstname+" "+self.lastname

class products(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(default=0,max_length=50)
    description = models.TextField()
    origin = models.CharField(max_length=50,default="Kenya")
    color = models.CharField(max_length=50,default="white")

    def __str__(self):
        return self.name