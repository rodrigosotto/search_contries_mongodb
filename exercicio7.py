from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

url_database = os.getenv("URL_MONGO_DB")

cliente = MongoClient(url_database)
banco_dados = cliente["countries_database"]
colecao = banco_dados["countries"]

try:
    # Consulta para encontrar as capitais que começam com a letra "W"
    resultado_consulta = colecao.find({"capital": {"$regex": "^W"}}, {"_id": 0, "capital": 1})

    print("Capitais que começam com a letra 'W':")
    for documento in resultado_consulta:
        print(documento["capital"])

except Exception as error:
    print("Erro ao consultar as capitais que começam com a letra 'W':", error)

# Fecha a conexão com o MongoDB
cliente.close()

# Este script utiliza a expressão regular ^W, onde ^ indica o início da string e W representa a letra "W". 
# Assim posso procurar por capitais cujo nome comece com a letra "W". 



