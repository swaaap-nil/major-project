import json
import threading
import asyncio
from pydantic import BaseModel
from spacy.matcher import PhraseMatcher
from fastapi import FastAPI, WebSocket
import numpy as np
import uvicorn
from typing import List
from SkillExtractor import skillExtractor
from rabbitmq import RabbitMQHelper
from database import companyWiseData, fetchDailyStatistics
from fastapi.middleware.cors import CORSMiddleware

class JobDescriptionRequest(BaseModel):
    job_description: str
    
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
active_connections: List[WebSocket] = []
rabbitmq=RabbitMQHelper()

@app.websocket("/jobfeed")
async def websocket_endpoint(websocket: WebSocket):
    """Handle WebSocket connections"""
    await websocket.accept()
    active_connections.append(websocket)
    try:
        while True:
            await websocket.receive_text()  # Keep connection alive
    except Exception:
        active_connections.remove(websocket)

async def broadcast(message: dict):
    """Send job updates to all connected WebSocket clients"""
    for connection in active_connections:
        try:
            await connection.send_json(message)
        except Exception:
            active_connections.remove(connection)

def rabbitmq_callback(message):
    """Callback function for RabbitMQ messages"""
    print(f"📩 [RabbitMQ] Received Job: {message}")
    asyncio.run(broadcast(message))  

def start_rabbitmq():
    thread = threading.Thread(target=rabbitmq.consume_messages, args=("notifications_queue", rabbitmq_callback), daemon=True)
    thread.start()

start_rabbitmq() 

@app.post("/extract-skills/")
def extract_skills(job_description: str):
    return skillExtractor.extractSkills(job_description) 

@app.get("/extract-skills-html/")
def extract_skills(job_description: str):
    return skillExtractor.extractSkillsHtml(job_description) 

@app.get("/daily-stats/")
def _():
    return fetchDailyStatistics()

@app.get("/company-wise-stats/")
def _():
    return companyWiseData()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
