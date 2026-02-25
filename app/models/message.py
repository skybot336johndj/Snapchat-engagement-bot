from pydantic import BaseModel

class MessageRequest(BaseModel):
    recipient_id: str
    message: str