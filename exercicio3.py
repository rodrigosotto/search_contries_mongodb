from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Obtém as variáveis de ambiente
url_database = os.getenv("URL_MONGO_DB")

# Conecta-se ao MongoDB
cliente = MongoClient(url_database)
banco_dados = cliente["countries_database"]
colecao = banco_dados["countries"]

try:
    # Agregação para listar todos os continentes distintos
    pipeline = [
        {"$group": {"_id": "$region"}},  # Agrupa os documentos pela região
        {"$match": {"_id": {"$ne": ""}}}  # Filtra para excluir strings vazias, caso existam regiões não especificadas
    ]
    resultado_agregacao = colecao.aggregate(pipeline)

    # Exibe o resultado
    print("Continentes Distintos:")
    for documento in resultado_agregacao:
        print(documento["_id"])

except Exception as error:
    print("Erro ao listar os continentes distintos:", error)

# Fecha a conexão com o MongoDB
cliente.close()
