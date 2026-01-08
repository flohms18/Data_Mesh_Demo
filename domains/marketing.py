from fastapi import FastAPI

app = FastAPI(title="Marketing Domain")

marketing_data = [
    {"campaign": "Email", "leads": 50},
    {"campaign": "Social", "leads": 120},
]

@app.get('/marketing')
def get_marketing_data():
    return {"data": marketing_data, "owner": "Marketing Team"}