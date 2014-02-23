from django.db import models

# Create your models here.
class Investor(models.Model):
     firstName = models.CharField(max_length=50,null=True,blank=True)
     lastName = models.CharField(max_length=50,null=True,blank=True)
     bio=models.TextField(null=True, blank=True)
     percCompleted=models.FloatField(default=0)
     pic=models.ImageField(upload_to="images/",blank=True, null=True)
     accountValue=models.FloatField(default=0)
     portfolioValue=models.FloatField(default=0)
     followers=models.IntegerField(default=0) #TBD - should point to other investors
     following=models.IntegerField(default=0) #TBD - should point to other investors
     syndicates=models.TextField(null=True, blank=True)
     statusUpdate=models.TextField(null=True, blank=True)
     portfolioReturn=models.FloatField(default=0)
     joiningDate=models.DateField(null=True)
    