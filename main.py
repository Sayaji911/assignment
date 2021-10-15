from fastapi import Depends,FastAPI
from src.models import Country

app = FastAPI()

@app.get("/")
async def root():
    return {
      "  Cricket Rest API"
    }
