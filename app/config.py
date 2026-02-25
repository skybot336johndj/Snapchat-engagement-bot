import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
OAUTH_CLIENT_ID = os.getenv("OAUTH_CLIENT_ID")
OAUTH_CLIENT_SECRET = os.getenv("OAUTH_CLIENT_SECRET")
GRAPH_API_URL = "https://api.snapchat.com/v1/messages"