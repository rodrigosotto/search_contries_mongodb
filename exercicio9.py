from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

url_database = os.getenv("URL_MONGO_DB")

cliente = MongoClient(url_database)
banco_dados = cliente["countries_database"]
colecao = banco_dados["countries"]

try:
    # Agregação para contar o número total de países no continente Ásia
    pipeline = [
        {"$match": {"region": "Asia"}},  # Filtra os documentos pelo continente Ásia
        {"$count": "total_paises"}  # Conta o número de documentos correspondentes
    ]
    resultado_agregacao = list(colecao.aggregate(pipeline))

    if resultado_agregacao:
        total_paises_asia = resultado_agregacao[0]["total_paises"]
        print("Total de países no continente Ásia:", total_paises_asia)
    else:
        print("Não foram encontrados países no continente Ásia.")

except Exception as error:
    print("Erro ao contar o número total de países no continente Ásia:", error)

cliente.close()

# Este script realiza as seguintes etapas:

# Filtragem por continente: Usa-se $match para filtrar os documentos pelo continente Ásia.
# Contagem de documentos: Utiliza-se $count para contar o número de documentos correspondentes após a filtragem.