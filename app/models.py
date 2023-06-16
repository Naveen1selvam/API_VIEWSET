from django.db import models

# Create your models here.
class Productcategory(models.Model):
    Cname=models.CharField(max_length=100)
    cid=models.IntegerField()

    def __str__(self) -> str:
        return self.Cname
    
class Product(models.Model):
    Cname=models.ForeignKey(Productcategory,on_delete=models.CASCADE)
    Pname=models.CharField(max_length=100)
    Pid=models.IntegerField()
    PriceP=models.IntegerField()

    def __str__(self) -> str:
        return self.Pname
