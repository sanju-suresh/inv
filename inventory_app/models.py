from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    studentid = models.CharField(max_length=200, null=True, blank=True)


class Category(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)


class Item(models.Model):
    cat_link = models.ForeignKey(Category, on_delete=models.CASCADE,blank=True, null=True)
    category = models.CharField(max_length=200, blank=True, null=True)
    item_name = models.CharField(max_length=200, blank=True, null=True)
    quantity = models.IntegerField(default=0)
    unqid = models.IntegerField(default=0)
    madeby = models.ForeignKey(Customer, on_delete=models.CASCADE,blank=True, null=True)
    created_number = models.IntegerField(default=0)

    def __str__(self):
        return self.item_name


class Issue(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    numberofitems = models.IntegerField(blank=False, null=False, default=0)
    returned = models.BooleanField(default=False)
    returnednum =  models.IntegerField(blank=True, null=True,default =0)


class Csv(models.Model):
    file_name = models.FileField(upload_to='csvs')
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f"File id: {self.id}"
