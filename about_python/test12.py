# -*- coding: utf-8 -*
import json
from datetime import datetime
import itertools
import time
f = open("./atest_read.txt")
#orders_loop.txt   orders_bellman.txt
f = open("orders_loop.txt")
f = open("orders_bellman.txt")
line = f.readline()
list1=[];
num_all=0
#定义查找数组
list2=[]
res2={}
#定义出现交易次数
num_all=0
#定义总交易量
profits=0
#定义不同单词出现次数的字典
res={}
#date_string = "2018-11-30 13:53:59.12121"
#print(time.strptime(date_string, "%Y-%m-%d %H:%M:%S:%f"))
#对时间进行转换
def str_time(timestr):
    time_1=time.strptime(timestr,"%Y-%m-%d %H:%M:%S.%f")
    datetime_obj= time.mktime(time_1)
#    print datetime_obj
    return int(datetime_obj)
# print 12
    #return obj_stamp
def loop_json(arr,time_int):
    for arr_num in arr:
        arr[arr_num]['time_add']=time_int
#        arr[arr_num]['key_tag']=arr[arr_num]['tradestring']+arr[arr_num]['equivalentprice']+arr[arr_num]['reverseprice']
        arr[arr_num]['key_tag']=arr[arr_num]['tradestring']+str(arr[arr_num]['equivalentprice'])+str(arr[arr_num]['reverseprice'])
def loop_list(list1,num_all,profits):
    for json_fs in list1:
#    i=++i
        for fs in json_fs:

             #判断tradestring 是否已经交易
            if json_fs[fs]['key_tag']  not in res2:
             # print json_fs[fs];
             #交易次数增加实现 
                 num_all=num_all+1
#利润增加实现   
                # profits=profits+ float(json_fs[fs]['equivalentprice'])*int(json_fs[fs]['volume']) - float(json_fs[fs]['reverseprice'])*int(json_fs[fs]['volume']) 
                 profits=profits+ (float(json_fs[fs]['equivalentprice']) - float(json_fs[fs]['reverseprice']))*int(json_fs[fs]['volume'])
                 #切割字符串得到单词组成数量 并把单词数添加到数组里
                 #对单词个数对应增加的次数进行计算
                 tradestring_vm= json_fs[fs]['tradestring'].split(":")
                 if len(tradestring_vm) not in res:
                     res[len(tradestring_vm)]=1
                 else:
                     res[len(tradestring_vm)]+=1
                 long_rt=len(tradestring_vm);
                 if  len(tradestring_vm)==8 :
                     print json_fs[fs]
                 #对tradestring 对应的单词进行循环排序
                 for num in range(0,len(tradestring_vm)):
                     tradestring_vm_cp=tradestring_vm[0];
                     for i in range(0,long_rt):
                         tradestring_vm[i%long_rt]=tradestring_vm[(1+i)%long_rt]
                     tradestring_vm[long_rt-1]=tradestring_vm_cp
#                 list2.extend(tradestring_vm)
                     strlj=''
                     for numm in range(0,len(tradestring_vm)):
                         if numm==0:
                             strlj=strlj+tradestring_vm[numm]
                         else:
                             strlj=strlj+":"+tradestring_vm[numm]
                     strlj=strlj+str(json_fs[fs]['equivalentprice'])+str(json_fs[fs]['reverseprice'])
                    # list2.append(strlj)
                     arr=[]
                     arr.append(json_fs[fs]['time_add'])
                     res2[strlj]=arr

                     #print strlj    
            else:

                time_cp= res2[json_fs[fs]['key_tag']]
                #print str(time_cp[0])
                tag_time=0
                for time_ls in time_cp:
                    if abs(json_fs[fs]['time_add']==time_cp)>5:
                        tag_time=1
                        time_cp.append(json_fs[fs]['time_add'])
                        break
                if tag_time==1:
                    #交易次数增加实现
num_all=num_all+1
                    #利润增加实现   
                    # profits=profits+ float(json_fs[fs]['equivalentprice'])*int(json_fs[fs]['volume']) - float(json_fs[fs]['reverseprice'])*int(json_fs[fs]['volume']) 
                    profits=profits+ (float(json_fs[fs]['equivalentprice']) - float(json_fs[fs]['reverseprice']))*int(json_fs[fs]['volume'])
    return num_all,profits
#读取文件
while line:
    line=line.strip('\n')
    line = line.split("!")
    time_int= str_time(line[0])
    line = json.loads(line[1])
    loop_json(line,time_int)
    list1.append(line)
   # print list1[0]['0']['tradetimes']
#    print list1    
    line = f.readline()
f.close()
num_all,profits=loop_list(list1,num_all,profits)
average=profits/num_all
#print list1
print 'orders : '+ str(num_all)
print 'profits : '+ str(profits)
print 'average:   '+str(average)
#print res
for key,value in res.items():
    print str(key)+"个单词出现次数："+ str(value)
   # print type(res_nu)

#print type(res)
print ''
#print list2
print len(res2)
                                                                                                                                                                                        123,1         Bot

