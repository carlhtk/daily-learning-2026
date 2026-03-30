import os 
from datetime import datetime 

from dotenv import load_dotenv 

load_dotenv()

def main():

    user = os.getenv("user_name", "ingeniero")
    now = datetime.now().strftime("%d/%m/%Y %H:%M")

    print(f"--- SISTEMA DE CONTROL ---")
    print(f"Bienvenido, {user}")
    print(f"Estado: Conectado")
    print(f"Fecha/Hora: {now}")
    print(f"--------------------------")

if __name__ == "__main__":
    main()
    