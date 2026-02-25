from fastapi import FastAPI
from app.routes import messaging, webhook

app = FastAPI(title="Snapchat Engagement API Automation")

app.include_router(messaging.router, prefix="/api")
app.include_router(webhook.router, prefix="/webhook")

@app.get("/")
def health_check():
    return {"status": "running"}