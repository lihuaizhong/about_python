# -*- coding: utf-8 -*
import json
import itertools
f = open("./atest_read.txt")
#orders_loop.txt   orders_bellman.txt
f = open("orders_loop.txt")
#f = open("orders_bellman.txt")
line = f.readline()
list1=[];
#读取文件
while line:
    line=line.strip('\n')
    line = line.split("!")
    line = json.loads(line[1])
    list1.append(line)
   # print list1[0]['0']['tradetimes']
    line = f.readline()
f.close()
#定义查找数组
list2=[]
#定义出现交易次数
num_all=0
#定义总交易量
profits=0
#定义不同单词出现次数的字典
res={}
for json_fs in list1:
#    i=++i
    for fs in json_fs:
         #判断tradestring 是否已经交易
         if json_fs[fs]['tradestring']  not in list2:
            # print json_fs[fs];
             #交易次数增加实现
             num_all=num_all+1
             #利润增加实现   
            # profits=profits+ float(json_fs[fs]['equivalentprice'])*int(json_fs[fs]['volume']) - float(json_fs[fs]['reverseprice'])*int(json_fs[fs]['volume']) 
             profits=profits+ (float(json_fs[fs]['equivalentprice']) - float(json_fs[fs]['reverseprice']))*int(json_fs[fs]['volume'])
             #切割字符串得到单词组成数量 并把单词数添加到数组里
             tradestring_vm= json_fs[fs]['tradestring'].split(":")
             if len(tradestring_vm) not in res:
                 res[len(tradestring_vm)]=1
             else:
                 res[len(tradestring_vm)]+=1
             long_rt=len(tradestring_vm);
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
                 list2.append(strlj)
                 print strlj
                   
average=profits/num_all
print 'orders : '+ str(num_all)
print 'profits : '+ str(profits)
print 'average:   '+str(average)
#print res
for key,value in res.items():
    print str(key)+"个单词出现次数："+ str(value)
   # print type(res_nu)

#print type(res)
leng = ['banana', 'apple',  'mango','cdcd','cda']
for num in range(0,len(leng)):
    leng_cp=leng[0];
    for i in range(0,len(leng)):
#        leng_cp=leng[0];
        leng[i%len(leng)]=leng[(i+1)%len(leng)]
    leng[len(leng)-1]=leng_cp
    #print leng
