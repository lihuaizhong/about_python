import requests
import json
def requests_name(url):
    r = requests.get(url)
#    print (r.text)
#def json_chuli(r.text)
    json_str = json.dumps(r.text)
#    print (json_str)
    params_json = json.loads(r.text)

    items = params_json.items()
    for key, value in items:
        #print(str(key) + '=' + str(value))
        print (value['lowestAsk']) 
url_pairs='https://data.gateio.co/api2/1/pairs'
url_marketinfo='https://data.gateio.co/api2/1/marketinfo'
url_tickers='https://data.gateio.co/api2/1/tickers'
requests_name(url_tickers)
