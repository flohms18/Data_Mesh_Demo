DATA_Products = {
    "sales": "http://127.0.0.1:8001/sales",
    "marketing": "http://127.0.0.1:8002/marketing"
}

def list_data_products():
    return list(DATA_Products.keys())

def get_product_url(name):
    return DATA_Products.get(name)