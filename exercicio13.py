from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

url_database = os.getenv("URL_MONGO_DB")

cliente = MongoClient(url_database)
banco_dados = cliente["countries_database"]
colecao = banco_dados["countries"]

try:
    # Agregação para somarizar o total de países por continente
    pipeline = [
        {"$group": {"_id": "$region", "total_paises": {"$sum": 1}}}  # Agrupa os documentos pelo continente e conta o total de países
    ]
    resultado_agregacao = colecao.aggregate(pipeline)

    # Exibe a sumarização
    print("Total de países por continente:")
    for documento in resultado_agregacao:
        print(documento["_id"], "-", documento["total_paises"])

except Exception as error:
    print("Erro ao somarizar o total de países por continente:", error)

cliente.close()
