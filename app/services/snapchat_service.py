import requests
from app.config import API_KEY, GRAPH_API_URL

def send_snap(recipient_id: str, message: str):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    payload = {
        "recipient": {"id": recipient_id},
        "message": {"text": message}
    }
    response = requests.post(GRAPH_API_URL, json=payload, headers=headers)
    return response.json()