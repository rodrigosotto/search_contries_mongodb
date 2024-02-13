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
    # Consulta para encontrar os 10 maiores países em área territorial
    resultado_consulta = colecao.find({}, {"_id": 0, "name.common": 1, "area": 1}).sort("area", -1).limit(10)

    print("Os 10 maiores países em área territorial:")
    for documento in resultado_consulta:
        print(documento["name"]["common"], "-", documento["area"], "km²")

except Exception as error:
    print("Erro ao consultar os 10 maiores países em área territorial:", error)

# Fecha a conexão com o MongoDB
cliente.close()
