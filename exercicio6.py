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
    # Consulta para obter as capitais na sub-região "South America"
    resultado_consulta = colecao.find({"subregion": "South America"}, {"_id": 0, "capital": 1})

    print("Capitais na sub-região 'South America':")
    for documento in resultado_consulta:
        print(documento["capital"])

except Exception as error:
    print("Erro ao consultar as capitais na sub-região 'South America':", error)

# Fecha a conexão com o MongoDB
cliente.close()
