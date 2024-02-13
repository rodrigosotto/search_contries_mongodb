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
    # Encontra o documento da França para obter os códigos dos países com os quais faz fronteira
    documento_franca = colecao.find_one({"cca3": "FRA"})
    if documento_franca and "borders" in documento_franca:
        codigos_fronteira = documento_franca["borders"]

        # Encontra os países que fazem fronteira com a França
        paises_fronteira = colecao.find({"cca3": {"$in": codigos_fronteira}}, {"_id": 0, "name.common": 1})

        print("Países que fazem fronteira com a França:")
        for pais in paises_fronteira:
            print(pais["name"]["common"])
    else:
        print("Não foi possível encontrar a França ou seus países de fronteira na coleção.")

except Exception as error:
    print("Erro ao consultar os países de fronteira:", error)

# Fecha a conexão com o MongoDB
cliente.close()
