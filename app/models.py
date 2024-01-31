from django.db import models

class YourModel(models.Model):
  name = models.CharField(max_length=255,null=True,)
  image = models.FileField(upload_to='members',max_length=255,null=True,blank=True,default=None)
  description = models.TextField(max_length=255,null=True,blank=True)
  def __str__(self):
    return f"{self.name}"
  
class Product(models.Model):
  name = models.CharField(max_length=255,null=True,)
  image = models.FileField(upload_to='members',max_length=255,null=True,blank=True,default=None)
  price = models.IntegerField(null=True,blank=True)
  def __str__(self):
    return f"{self.name}"