from django.db import models

# Create your models here.
# class Info(models.Model):
#     fname = models.CharField(max_length = 30)
#     lname = models.CharField(max_length = 30)
#     number = models.CharField(max_length = 30)
#     address = models.TextField()
#     date = models.DateField()

class Payment(models.Model):
    fullname = models.CharField(max_length = 40)
    email = models.CharField(max_length = 25)
    address = models.TextField()
    city = models.CharField(max_length = 20)
    state = models.CharField(max_length = 20)
    zipcode = models.CharField(max_length = 6)
    name = models.CharField(max_length = 40)
    ccnumber = models.CharField(max_length = 40)
    expirymonth = models.CharField(max_length = 40)
    expiryyear = models.CharField(max_length = 40)
    cvv = models.CharField(max_length = 3)

class Contact(models.Model):
    fname = models.CharField(max_length = 20)
    lname = models.CharField(max_length = 20)
    mail = models.CharField(max_length = 25)
    phone = models.CharField(max_length = 20)
    message = models.TextField()
    