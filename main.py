import random
import time
import json
import urllib.request
from prometheus_client import start_http_server, Gauge
from config import *


rohlik_product_price_metric = Gauge('rohlik_produkt_price', 'Rohlik product price.', ["product_id", "product_name"])


def get_product(product_id):
    req_price = urllib.request.Request(f'https://www.rohlik.cz/api/v1/products/{product_id}/prices')
    req_price.add_header('User-Agent', user_agent)
    r_price = urllib.request.urlopen(req_price)

    req_product = urllib.request.Request(f'https://www.rohlik.cz/api/v1/products/{product_id}')
    req_product.add_header('User-Agent', user_agent)
    r_product = urllib.request.urlopen(req_product)

    result_price = json.loads(r_price.read())
    result_product = json.loads(r_product.read())

    if len(result_price['sales'])>0:
        price = result_price['sales'][0]['price']['amount']
    else:
        price = result_price['price']['amount']
    name = result_product['name']

    return price, name

if __name__ == '__main__':
    start_http_server(8000)

    while True:
        for p in products:
            price, name = get_product(p)
            rohlik_product_price_metric.labels(p, name).set(price)
        time.sleep(interval)
