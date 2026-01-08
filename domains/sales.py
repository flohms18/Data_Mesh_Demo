from fastapi import FastAPI

app = FastAPI(title="Sales Domain")


sales_data = [
    {"order_id": 1, "amount": 100, "customer": "Alice"},
    {"order_id": 2, "amount": 200, "customer": "Bob"},
]

app.get('/sales')
def get_sales_data():
   return {"data": sales_data, "owner": "Sales Team"}