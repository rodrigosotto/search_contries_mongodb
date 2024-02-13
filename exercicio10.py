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
    # Consulta para encontrar países cujo idioma oficial é "Danish" no campo "languages"
    resultado_consulta = colecao.find({"languages.dan": "Danish"}, {"_id": 0, "name.common": 1})

    print("Países cujo idioma oficial é 'Danish':")
    for documento in resultado_consulta:
        print(documento["name"]["common"])

except Exception as error:
    print("Erro ao consultar os países cujo idioma oficial é 'Danish':", error)

# Fecha a conexão com o MongoDB
cliente.close()
