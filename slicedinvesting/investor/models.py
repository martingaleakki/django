from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group as DjangoGroup
from django.db.models.signals import post_save

# Create your models here.

class InvestorProfile(models.Model):
    
     username = models.CharField(max_length=50,primary_key=True)
     user = models.OneToOneField(User,related_name='profile')
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
     
     @models.permalink
     def get_absolute_url(self):
        return ('profiles_profile_detail', (), { 'username': self.username })
    
    
     def __unicode__(self):
        return self.pk
    
     def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in InvestorProfile._meta.fields]
     


def create_investor(sender, **kwargs):
    """When creating a new user, make him an investor and create an empty profile for him or her."""
    u = kwargs["instance"]
    try:
        
        if not InvestorProfile.objects.filter(username=u.username):
            inv = InvestorProfile(username=u.username,user=u)
            inv.save()
            g = DjangoGroup.objects.get(name='Investors') 
            g.user_set.add(u)
    except Exception as e:
        print e       

post_save.connect(create_investor, sender=User)

     

    