from fastapi import APIRouter, Request
from app.config import API_KEY

router = APIRouter()

@router.get("/")
def verify_webhook(mode: str = None, verify_token: str = None, challenge: str = None):
    if mode == "subscribe" and verify_token == API_KEY:
        return int(challenge)
    return {"error": "Verification failed"}

@router.post("/")
async def receive_webhook(request: Request):
    payload = await request.json()
    return {"status": "received", "event": payload}