import configuration
import requests
import data
def post_products_kits(products_ids):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
headers=data.headers)
response = post_products_kits();
print(response.status_code/ + response.json())
