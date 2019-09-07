import os

from dotenv import load_dotenv as ld

ld()


class Config:
    API_KEY = os.environ.get("API_KEY")
