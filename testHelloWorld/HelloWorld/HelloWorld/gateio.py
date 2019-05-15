import json
import requests 

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
