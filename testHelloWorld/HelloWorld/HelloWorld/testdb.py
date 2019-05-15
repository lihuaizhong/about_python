# -*- coding: utf-8 -*-
import requests
import sys
import json
import io
import time
import redis
#from ./  gateio *
from django.http import HttpResponse
from TestModel.models import Test
from TestModel.models import customer
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
 # 数据库操作添加数据
def testdbsave(request):
    list_name= requests_name(url_marketlist,'EOS')
    for list_nameli in list_name:
#        test1 = Test(name='runoob',name_cn=list_nameli['name_cn'])
        test1 = customer(name=list_nameli['name_en'],name_cn=list_nameli['name_cn'],pair=list_nameli['pair'],rate=list_nameli['rate'])
        print (list_nameli)
        test1.save()
    list_name= requests_name(url_marketlist,'EOS')
    return HttpResponse("<p>数据添加成功！</p>")
#    return HttpResponse("<p>数据添加成功！</p>"+"".join(list_name))
#删除数据
def testdbdelete(request):
    # 删除id=1的数据
    test1 = Test.objects.get(id=1)
    test1.delete()

    # 另外一种方式
    # Test.objects.filter(id=1).delete()

    # 删除所有数据
    # Test.objects.all().delete()

    return HttpResponse("<p>删除成功</p>")
# 数据库操作更新数据
def testdbgengxin(request):
    # 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
#    test1 = Test.objects.get(id=1)
#    test1 = Test.objects.get(pair='eos_usdt')
#    test1.name = 'Google'
#    test1.save()
    list_name= requests_name(url_marketlist,'EOS')
    print (list_name)
    num=True;
    while num:
        list_name= requests_name(url_marketlist,'EOS') 
        for list_nameli in list_name:
            time.sleep(0.01)
            #对键值对进行搜索
            test1 = Test.objects.get(pair=list_nameli['pair'])
            #test1 = Test(name='runoob',name_cn=list_nameli['name_cn'],now_time=str(time.time()))
            print('-----------------------')
            print (test1.rate)
#            print('-----------------------')
            test1.rate =list_nameli['rate']
           # test1.now_time = Test(time.time()
#            srt_tag=  redis_get(list_nameli['name_cn'])
            srt_tag=  redis_get(list_nameli['pair'])
            print (str(srt_tag)=='None')
            if str(srt_tag)=='None' :
                ret=redis_genxin(list_nameli['pair'],list_nameli['rate'])
            else :
                if srt_tag==list_nameli['rate'] :
                    pass
                else :
                    redis_genxin(list_nameli['pair'],list_nameli['rate'])   
#            print (list_nameli)
            
            test1.save()
#            num=False;
            num=True
#            print(time.time()) 
    # 另外一种方式
    #Test.objects.filter(id=1).update(name='Google')

    # 修改所有的列
    # Test.objects.all().update(name='Google')

    return HttpResponse("<p>修改成功</p>")
# 数据库操作 获取数据
def testdbget(request):
    # 初始化
    response = ""
    response1 = ""


    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = Test.objects.all()

    # filter相当于SQL中的WHERE，可设置条件过滤结果
    response2 = Test.objects.filter(id=1)

    # 获取单个对象
    response3 = Test.objects.get(id=1)

    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    Test.objects.order_by('name')[0:2]

    #数据排序
    Test.objects.order_by("id")

    # 上面的方法可以连锁使用
    Test.objects.filter(name="runoob").order_by("id")

    # 输出所有数据
    for var in list:
        response1 += var.name + " "
    response = response1
    return HttpResponse("<p>" + response + "</p>")
def redis_get(str_name):
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)   # host是redis主机，需要redis服务端和客户端都启动 redis默认端口是6379
    str_tag=r.get(str_name)
    print (str_tag)
    return str_tag
def redis_set(str_name,pri):
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)   # host是redis主机，需要redis服务端和客户端都启动 redis默认端口是6379
    str_tag=r.set('str_name',pri)
    print (' redis_set')
    return str_tag
def redis_genxin(str_name,price):
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)   # host是redis主机，需要redis服务端和客户端都启动 redis默认端口是6379
    str_tag=r.set(str_name,price)
    ps = r.pubsub()
 
    ps.subscribe(['foo', 'bar'])  #订阅两个频道
 
    r.publish('foo', price)
    print ('redis_genxin')
    return str_tag
url_marketlist='https://data.gateio.co/api2/1/marketlist'
def requests_name(url,currency):
    r = requests.get(url)
    name_list=list()
    json_str = json.dumps(r.text)
    params_json = json.loads(r.text)
    items = params_json.items()
    for key, value in items:
        if (type(value))==list:
            for value1 in  value :
                if value1['name']==currency:
#                    print(value1)
#                    name_list.append(value1['rate'])
                    name_list.append(value1)
                    print ( value1['name'] +" "+ value1["pair"]+": "+value1['rate'])      
    return name_list
#requests_name(url_marketlist,'EOS')                                               
