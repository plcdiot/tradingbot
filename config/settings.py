from dataclasses import dataclass
import os

@dataclass
class Settings:
    api_key: str = os.getenv("KITE_API_KEY","")
    access_token: str = os.getenv("KITE_ACCESS_TOKEN","")
    environment: str = os.getenv("ENV","dev")
