from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

url_database = os.getenv("URL_MONGO_DB")

cliente = MongoClient(url_database)
banco_dados = cliente["countries_database"]
colecao = banco_dados["countries"]

try:
    # Consulta para encontrar países com três idiomas oficiais
    resultado_consulta = colecao.find({"$expr": {"$eq": [{"$size": {"$objectToArray": "$name.native"}}, 3]}}, {"_id": 0, "name.common": 1})

    print("Países que possuem 3 idiomas oficiais:")
    for documento in resultado_consulta:
        print(documento["name"]["common"])

except Exception as error:
    print("Erro ao consultar os países que possuem 3 idiomas oficiais:", error)

cliente.close()
