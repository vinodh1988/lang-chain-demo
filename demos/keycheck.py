from keyexport import openkey
from dotenv import  load_dotenv
import os

print(openkey)

load_dotenv()

print(os.getenv('OPEN_KEY'))