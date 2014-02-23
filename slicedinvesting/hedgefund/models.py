from django.db import models

# Create your models here.


class HedgeFund(models.Model):
    name = models.CharField(max_length=50,null=True)
    type= models.CharField(max_length=50,null=True)
    description=models.TextField(null=True, blank=True)
    percCompleted=models.FloatField(default=0)
    portfolioManager=models.CharField(max_length=50,null=True, blank=True)
    numYearsActive=models.FloatField(default=0) #TBD This can be backed out from Origin Date
    assetsUnderManagement=models.IntegerField(default=0)
    managementFees=models.FloatField(default=0)
    performanceFees=models.FloatField(default=0)
    lockInPeriod=models.FloatField(default=0)
    reportingFrequency=models.IntegerField(default=0) #TBD Should be of Type- Enum
    capitalRequested=models.FloatField(default=0)
    capitalRaised=models.FloatField(default=0)
    parentSyndicates=models.TextField(null=True, blank=True) #TDB Syndicate class
    numLikes=models.IntegerField(default=0)
    hotness=models.IntegerField(default=0)
    returnMetrics=models.FloatField(default=0) #TBD This has to be a class
    originDate=models.DateField(null=True)
    website=models.TextField(null=True)