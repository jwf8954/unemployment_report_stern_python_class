
import os
from dotenv import load_dotenv

load_dotenv()           # this looks in the .env file 

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="demo")