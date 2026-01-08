from fastapi import FastAPI, HTTPException
import httpx
from registry import DATA_Products, list_data_products, get_product_url

app = FastAPI(title="Central Data Mesh")

@app.get('/products')
def products():
    """List available data products"""
    return {"products": list_data_products()}

@app.get("/products/{product_name}")
def fetch_product(product_name: str):
    """Fetch data from a specific domain"""
    url = get_product_url(product_name)
    if not url:
        raise HTTPException(status_code=404, detail="Data product not found")
    
    try:
        response = httpx.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=str(e))