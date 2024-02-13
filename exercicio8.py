from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

url_database = os.getenv("URL_MONGO_DB")

cliente = MongoClient(url_database)
banco_dados = cliente["countries_database"]
colecao = banco_dados["countries"]

try:
    # Agregação para contar o número de vezes que cada idioma aparece
    pipeline = [
        {"$project": {"idiomas": {"$objectToArray": "$languages"}}},  # Transforma o dicionário de idiomas em um array de valores
        {"$unwind": "$idiomas"},  # Desagrega o array para que cada idioma seja um documento
        {"$group": {"_id": "$idiomas.v", "total": {"$sum": 1}}},  # Agrupa os documentos pelo idioma e conta o total de ocorrências
        {"$sort": {"total": -1}}  # Ordena os resultados em ordem decrescente
    ]
    resultado_agregacao = colecao.aggregate(pipeline)

    # Exibe o ranking dos idiomas mais falados
    print("Ranking dos idiomas mais falados:")
    for documento in resultado_agregacao:
        print(documento["_id"], "-", documento["total"])

except Exception as error:
    print("Erro ao criar o ranking dos idiomas mais falados:", error)

# Fecha a conexão com o MongoDB
cliente.close()

# Este script realiza as seguintes etapas:
# Transforma o dicionário de idiomas em um array de valores: Isso é necessário para poder manipular mais facilmente os valores dos idiomas.
# Desagrega o array: Cada idioma se torna um documento separado, o que facilita a contagem.
# Agrupa os documentos pelo idioma e conta o total de ocorrências: Usa-se $group para agrupar os documentos pelo idioma e $sum para contar quantas vezes cada idioma aparece.
# Ordena os resultados em ordem decrescente: Usando $sort, os resultados são classificados com base no total de ocorrências em ordem decrescente.