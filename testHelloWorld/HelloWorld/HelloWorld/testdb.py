# -*- coding: utf-8 -*-
import requests
import sys
import json
import io
import time
from django.http import HttpResponse

from TestModel.models import Test
 # 数据库操作添加数据
def testdbsave(request):
    list_name= requests_name(url_marketlist,'EOS')
    for list_nameli in list_name:
        test1 = Test(name='runoob',name_cn=list_nameli['name_cn'])
        test1 = Test(name=list_nameli['name_en'],name_cn=list_nameli['name_cn'],pair=list_nameli['pair'],rate=list_nameli['rate'])
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
    while True: 
        for list_nameli in list_name:
            time.sleep(0.01)
            test1 = Test.objects.get(pair=list_nameli['pair'])
            #test1 = Test(name='runoob',name_cn=list_nameli['name_cn'])
            test1.rate =list_nameli['rate']
            print (list_nameli)
            test1.save()
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
