import requests
from urllib.parse import urljoin

HOST = 'http://wp8m3he1wt.s3-website-ap-southeast-2.amazonaws.com'
ENDPOINT = '/api/products/1'
INDUSTRY_WEIGHT_FACTOR = 250

def calculate_weight(category):
    return retrieve_category_weights(category)

def retrieve_category_weights(category):
    weights_list = []
    session = requests.Session()
    endpoint = ENDPOINT  
    while True:
        answer = session.get(urljoin(HOST, endpoint))
        endpoint = answer.json()['next']
        weights_list.extend(extract_weights_for_category_from_json(json=answer.json()['objects'], category=category))
        if not endpoint:
            break
    return sum(weights_list)

def extract_weights_for_category_from_json(json, category):
    return [calculate_weight_from_size(x["size"]) for x in json if x["category"]==category]

def calculate_weight_from_size(size_dict):
    width = size_dict["width"]/100.0
    length = size_dict["length"]/100.0
    height = size_dict["height"]/100.0
    return width*length*height*INDUSTRY_WEIGHT_FACTOR