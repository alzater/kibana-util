import requests
import readline


def open_index(host, index):
    url = 'http://'+host+"/"+index+"/_open"
    response = requests.post(url)
    print "status_code:", response.status_code, " response:", response.text

    
def close_index(host, index):
    url = 'http://'+host+"/"+index+"/_close"
    response = requests.post(url)
    print "status_code:", response.status_code, " response:", response.text


def create_index(host, index):
    url = 'http://'+host+"/"+index
    request =  '{"settings" : {"number_of_shards" : 1}}'
    response = requests.put(url, request)
    print "status_code:", response.status_code, " response:", response.text

  
def delete_index(host, index):
    url = 'http://'+host+"/"+index
    response = requests.delete(url)
    print "status_code:", response.status_code, " response:", response.text
 
def ask_delete_index(host, index):
    print "Delete index ["+index+']? '
    res = raw_input('Input "yes" for accept:\n')
    if res == 'yes':
        delete_index(host, index)
    else:
        print "Not deleted."
    
    
def split_line(line):
    result = []
    str=''
    for char in line:
        if char == ' ':
            if str!='':
                result.append(str)
                str = ''
            continue
        str += char
    return result
    

def parse_indices(data):
    lines = data.split('\n')
    result = []
    first_line = split_line(lines.pop(0))
    for line in lines:
        result.append(split_line(line))
    
    return result


def get_indices(host):
    url = 'http://'+host+"/_cat/indices?v&bytes=b"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print "Index exists check failed: code:", response.status_code
        return None
    
    
def create_index(host, index):
    url = 'http://'+host+"/"+index
    response = requests.head(url)
    if response.code == 200:
        return True
    elif response.code == 400:
        return False
    else:
        print "Index exists check failed: code:", response.code
        return False


def change_mapping(host, index, itype, changing):
    request = '{"'+itype+'":{"properties":'+changing+'}}'
    print request
    url = 'http://'+host+"/"+index+"/_mapping/"+itype
    response = requests.put(url, request)
    print "result:", response.text


def preaty_num(num):
    result = ''
    i = 0
    while num > 0:
        if i == 3:
            result = ',' + result
            i = 0
        result = str(num % 10) + result
        num /= 10
        i += 1
    return result        


def test1(host, index):
    request = '{ "size": 0, "query": { "filtered": { "query": { "query_string": { "query": "*", "analyze_wildcard": true } }, "filter": { "bool": { "must": [ { "range": { "datetime": { "gte": 1477774800000, "lte": 1477861199999, "format": "epoch_millis" } } } ], "must_not": [] } } } }, "aggs": { "1": { "scripted_metric": { "init_script": "_agg[\'transactions\'] = []", "map_script": "_agg.transactions.add(doc[\'amount\'].value)", "combine_script": "profit = 0; for (t in _agg.transactions) { profit += t }; return profit", "reduce_script": "profit = 0; for (a in _aggs) { profit += a }; return profit" } } } } '


    url = 'http://'+host+"/"+index+"/dmplog/_search?&pretty=true&size=3"
    response = requests.post(url, request)
    print "result:", response.text
    
            


 


 
