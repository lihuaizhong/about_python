from django.db import models
import time
# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=100,null=True)
    name_cn = models.CharField(max_length=200,null=True,verbose_name='test')
    rate = models.CharField(max_length=200,null=True,verbose_name='test1') 
    pair = models.CharField(max_length=200,null=True,verbose_name='test2')
    now_time= models.CharField(max_length=200,null=True,verbose_name='test2')
class customer(models.Model):
#    id = models.CharField(max_length=30)
    name = models.CharField(max_length=100,null=True)
    name_cn = models.CharField(max_length=200,null=True,verbose_name='test')
    rate = models.CharField(max_length=200,null=True,verbose_name='test1')
    pair = models.CharField(max_length=200,null=True,verbose_name='test2')
    now_time= models.CharField(max_length=200,null=True,verbose_name='test2')     
    class Meta:
        print (time.strftime("%Y-%m-%d", time.localtime()))
        db_table='2019_05_15'
