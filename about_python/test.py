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
num=0
#定义总交易量
profits=0
#定义不同单词出现次数的数组
res={}
for json_fs in list1:
#    i=++i
    for fs in json_fs:
         #判断tradestring 是否已经交易
         if json_fs[fs]['tradestring']  not in list2:
            # print json_fs[fs];
             #交易次数增加实现
             num=num+1        
             #利润增加实现   
            # profits=profits+ float(json_fs[fs]['equivalentprice'])*int(json_fs[fs]['volume']) - float(json_fs[fs]['reverseprice'])*int(json_fs[fs]['volume']) 
             profits=profits+ (float(json_fs[fs]['equivalentprice']) - float(json_fs[fs]['reverseprice']))*int(json_fs[fs]['volume']) 
             #切割字符串得到单词组成数量 并把单词数添加到数组里
             tradestring_vm= json_fs[fs]['tradestring'].split(":")
             if len(tradestring_vm) not in res:
                 res[len(tradestring_vm)]=1
             else:
                 res[len(tradestring_vm)]+=1
             if len(tradestring_vm)==3:
                 #对第一次三个单词的交易，对单词进行有序排序，然后存到数组里
                 list3=list(itertools.permutations([tradestring_vm[0],tradestring_vm[1],tradestring_vm[2]],3)) 
                 for item in list3:
                     srt=item[0]+":"+item[1]+":"+item[2]
                     list2.append(srt)
             else:
                 list2.append(json_fs[fs]['tradestring'])
average=profits/num
print 'orders : '+ str(num)     
print 'profits : '+ str(profits)
print 'average:   '+str(average)
#print res
for key,value in res.items():
    print str(key)+"个单词出现次数："+ str(value)
   # print type(res_nu)

#print type(res)
