#-*-coding:utf-8 -*-
import requests
import sys
import json
import io
def requests_name_xj(input_list) :
    for i, val in enumerate(input_list, 0):
       
#        print ("序号：%s   值：%s" % (i + 1, sys.argv[i]))
        requests_name(url_marketlist,input_list[i])
def requests_name_list(url,name_list):
    r = requests.get(url)
    json_str = json.dumps(r.text)
    params_json = json.loads(r.text)
    items = params_json.items()
    for key, value in items:
        if (type(value))==list:
            for value1 in  value :
#                if value1['name']=='Ethereum':
                name_list.append(value1['name'])                
def requests_name(url,currency):
    r = requests.get(url)
    json_str = json.dumps(r.text)
    params_json = json.loads(r.text)
    items = params_json.items()
    for key, value in items:
        if (type(value))==list:
            for value1 in  value :
                if value1['name']==currency:
#                    print(value1)
                    print ( value1['name'] +" "+ value1["pair"]+": "+value1['rate'])
url_pairs='https://data.gateio.co/api2/1/pairs'
url_marketinfo='https://data.gateio.co/api2/1/marketinfo'
url_tickers='https://data.gateio.co/api2/1/tickers'
url_eth_btc='https://data.gateio.co/api2/1/ticker/eth_btc'
url_marketlist='https://data.gateio.co/api2/1/marketlist'
#requests_name(url_tickers)
#requests_name(url_eth_btc)
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
name_list=list()
requests_name_list(url_marketlist,name_list)
print (name_list)
a = input("可以查询以上的货币，（Ethereum EOS Monero Bitcoin..........................）请输入你要查看的货币:")
a= a.split()
print (a)
requests_name_xj(a)
#requests_name(url_marketlist,'Ethereum')
