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
    # Agregação para listar todos os idiomas distintos
    pipeline = [
        {"$project": {"idiomas": {"$objectToArray": "$languages"}}},  # Transforma o dicionário de idiomas em um array de valores
        {"$unwind": "$idiomas"},  # Desagrega o array para que cada idioma seja um documento
        {"$group": {"_id": None, "todos_idiomas": {"$addToSet": "$idiomas.v"}}},  # Agrupa todos os documentos e coleta idiomas distintos
        {"$project": {"_id": 0, "todos_idiomas": 1}}  # Formata a saída para mostrar apenas a lista de idiomas
    ]
    resultado_agregacao = colecao.aggregate(pipeline)

    # Exibe o resultado
    for documento in resultado_agregacao:
        print("Idiomas distintos:", documento["todos_idiomas"])

except Exception as error:
    print("Erro ao listar os idiomas distintos:", error)

# Fecha a conexão com o MongoDB
cliente.close()
