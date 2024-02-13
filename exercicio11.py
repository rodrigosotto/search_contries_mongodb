from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

url_database = os.getenv("URL_MONGO_DB")

cliente = MongoClient(url_database)
banco_dados = cliente["countries_database"]
colecao = banco_dados["countries"]

try:
    # Agregação para contar o número de vezes que cada moeda aparece
    pipeline = [
        {"$unwind": "$currency"},  # Desagrega o array de moedas para que cada moeda seja um documento
        {"$group": {"_id": "$currency", "total": {"$sum": 1}}},  # Agrupa os documentos pela moeda e conta o total de ocorrências
        {"$sort": {"total": -1}}  # Ordena os resultados em ordem decrescente
    ]
    resultado_agregacao = colecao.aggregate(pipeline)

    # Exibe o ranking das moedas mais utilizadas
    print("Ranking das moedas mais utilizadas:")
    for documento in resultado_agregacao:
        print(documento["_id"], "-", documento["total"])

except Exception as error:
    print("Erro ao criar o ranking das moedas mais utilizadas:", error)

cliente.close()
