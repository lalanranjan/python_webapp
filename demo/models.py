from django.db import models

# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=20,unique=True,null=True)
    email=models.EmailField(unique=True)
    phone=models.IntegerField(max_length=10,null=True)
    Address=models.TextField(null=True)
    slug=models.SlugField(default="")

    def __str__(self):
        return self.name