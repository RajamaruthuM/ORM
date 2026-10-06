from django.db import models
from django.contrib import admin
class bikeservice_DB(models.Model):
    Vehicle_no=models.CharField(primary_key=True,max_length=8)
    Name=models.CharField(max_length=10)
    DoR=models.DateField()
    Address=models.TextField()
    Mobile=models.IntegerField()
    Vehicle_model=models.CharField(max_length=6)

class bikeservice_DBAdmin(admin.ModelAdmin):
    list_display=["Vehicle_no","Name","DoR","Address","Mobile","Vehicle_model"]