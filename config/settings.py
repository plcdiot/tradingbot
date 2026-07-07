from dataclasses import dataclass
from dotenv import load_dotenv
import os

load_dotenv()

@dataclass(slots=True)
class Settings:
    api_key:str=os.getenv("KITE_API_KEY","")
    api_secret:str=os.getenv("KITE_API_SECRET","")
    access_token:str=os.getenv("KITE_ACCESS_TOKEN","")
    environment:str=os.getenv("ENV","dev")
