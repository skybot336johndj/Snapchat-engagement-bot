from fastapi import APIRouter, HTTPException
from app.services.snapchat_service import send_snap
from app.models.message import MessageRequest

router = APIRouter()

@router.post("/send")
def send_snap_message(payload: MessageRequest):
    response = send_snap(payload.recipient_id, payload.message)
    if response.get("error"):
        raise HTTPException(status_code=400, detail=response)
    return {"status": "sent", "response": response}