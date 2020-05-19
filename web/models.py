from django.db import models

# Create your models here.
class subsciption(models.Model):
    s_types = [
        ('FREE', 'Free'),
        ('PRO', 'Pro'),
        ('ENTERPRISE', 'Enterprise'),
    ]
    support = [
        ('No Support', 'No Support'),
        ('Email Support', 'Email Support'),
        ('Call & Email Support', 'Call & Email Support'),
    ]

    center_support = [
        ('Help Docs. Access', 'Help Docs. Access'),
    ]
    price =  models.IntegerField()
    user = models.CharField(max_length=15)
    gb = models.CharField(max_length=8)
    s_type = models.CharField(max_length=10 ,choices=s_types, default= 'FREE')
    support = models.CharField(max_length=30, choices=support, default='NO SUPPORT')
    center_support = models.CharField(max_length=30, choices=center_support, default='Help Docs. Access')


    
    def __str__(self):
        return self.gb




class subscriber(models.Model):
    s_types = [
        ('FREE', 'Free'),
        ('PRO', 'Pro'),
        ('ENTERPRISE', 'Enterprise'),
    ]
    support = [
        ('No Support', 'No Support'),
        ('Email Support', 'Email Support'),
        ('Call & Email Support', 'Call & Email Support'),
    ]

    center_support = [
        ('Help Docs. Access', 'Help Docs. Access'),
    ]
    price =  models.IntegerField()
    user = models.CharField(max_length=15)
    gb = models.CharField(max_length=8)
    s_type = models.CharField(max_length=10 ,choices=s_types, default= 'FREE')
    support = models.CharField(max_length=30, choices=support, default='NO SUPPORT')
    center_support = models.CharField(max_length=30, choices=center_support, default='Help Docs. Access')


    
    def __str__(self):
        return self.gb


    