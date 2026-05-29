from dotenv import load_dotenv
import os

load_dotenv()

SENHA_AUTH = os.getenv("SECRET_KEY")
ASSINATURA_JWT= os.getenv("ALGORITHM")