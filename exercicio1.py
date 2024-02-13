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
    # Agregação para listar todos os nomes dos países
    pipeline = [
        {"$project": {"_id": 0, "nome_pais": "$name.common"}}
    ]
    resultado_agregacao = colecao.aggregate(pipeline)

    # Itera sobre o resultado da agregação e imprime cada nome de país
    for documento in resultado_agregacao:
        print(documento.get("nome_pais"))
    
    total_paises = colecao.count_documents({})
    print("Total de países na base:", total_paises)

except Exception as error:
    print("Erro ao listar os nomes dos países:", error)
    print("Erro ao contar o total de países:", error)

# Fecha a conexão com o MongoDB
cliente.close()
