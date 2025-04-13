from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import os
from .calculation import PaymentCalculator

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount the frontend directory
app.mount("/static", StaticFiles(directory="frontend"), name="static")

class PaymentInput(BaseModel):
    hourly_rate_usd: float
    hours_per_day: float
    working_days_per_week: int = 5

@app.get("/")
async def root():
    return FileResponse('frontend/index.html')

@app.get("/styles.css")
async def get_styles():
    return FileResponse('frontend/styles.css')

@app.get("/script.js")
async def get_script():
    return FileResponse('frontend/script.js')

@app.post("/api/calculate")
async def calculate_earnings(input_data: PaymentInput):
    try:
        calculator = PaymentCalculator()
        results = calculator.calculate_earnings(
            hourly_rate_usd=input_data.hourly_rate_usd,
            hours_per_day=input_data.hours_per_day,
            working_days_per_week=input_data.working_days_per_week
        )
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 