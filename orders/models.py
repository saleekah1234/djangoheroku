from django.db import models


class Order(models.Model):
    Name=models.TextField(max_length=35)
    #phone=models.PhoneField(blank=True, help_text='Contact phone number')
    Item=models.TextField(max_length=35)
    Quantity=models.TextField(max_length=35)
    Phonenumber=models.TextField(max_length=35)
    





# Create your models here.
