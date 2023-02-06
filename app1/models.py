from django.db import models
class submit(models.Model):
    Name=models.CharField(max_length=20)
    Age=models.IntegerField()
    Place=models.CharField(max_length=20)
    Email=models.EmailField()
    Password=models.CharField(max_length=20)
    Photo=models.ImageField(upload_to='media/',null=True,blank=True)


class Images(models.Model):
    Name=models.CharField(max_length=20)
    Age=models.IntegerField()
    Place=models.CharField(max_length=20)
    Email=models.EmailField()
    Password=models.CharField(max_length=20)
    Photo=models.ImageField(upload_to='media/',null=True,blank=True)

class ImagesT(models.Model):
    Name=models.CharField(max_length=20)
    Brand=models.CharField(max_length=20)
    Model=models.CharField(max_length=20)
    Photo=models.ImageField(upload_to='media/',null=True,blank=True)

