from fastapi import FastAPI
import uvicorn
import json

app = FastAPI()

# Load sample drug database (dummy data for now)
with open("models/drug_data.json", "r") as f:
    drug_db = json.load(f)

@app.get("/")
def home():
    return {"message": "Backend is running"}

@app.post("/check_drug")
def check_drug(drug: str):
    if drug in drug_db:
        return {"drug": drug, "info": drug_db[drug]}
    return {"error": "Drug not found"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)