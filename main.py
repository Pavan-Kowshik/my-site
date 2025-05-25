from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load data once
with open("data.json", "r") as f:
    raw_data = json.load(f)

# Convert list to dictionary for faster lookups
marks_data = {entry["name"]: entry["marks"] for entry in raw_data}

@app.get("/api")
def get_marks(name: list[str] = []):
    return {"marks": [marks_data.get(n, 0) for n in name]}
