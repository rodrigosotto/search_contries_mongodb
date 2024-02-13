from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

url_database = os.getenv("URL_MONGO_DB")

cliente = MongoClient(url_database)
banco_dados = cliente["countries_database"]
colecao = banco_dados["countries"]

try:
    # Consulta para encontrar países cuja moeda oficial é o dólar
    resultado_consulta = colecao.find({"currency": "USD"}, {"_id": 0, "name.common": 1})

    print("Países cuja moeda oficial é o dólar:")
    for documento in resultado_consulta:
        print(documento["name"]["common"])

except Exception as error:
    print("Erro ao consultar os países cuja moeda oficial é o dólar:", error)

cliente.close()
