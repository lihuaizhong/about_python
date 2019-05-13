from django.db import models

# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=20,null=True)
    name_cn = models.CharField(max_length=20,null=True,verbose_name='test')
    rate = models.CharField(max_length=20,null=True,verbose_name='test1') 
    pair = models.CharField(max_length=20,null=True,verbose_name='test2')
    now_time= models.CharField(max_length=20,null=True,verbose_name='test2')
