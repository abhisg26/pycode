from dotenv import load_dotenv
import os

load_dotenv('.env')

username: str = os.getenv('USERNAME')
password: str = os.getenv('PASSWORD')

print(username,password)