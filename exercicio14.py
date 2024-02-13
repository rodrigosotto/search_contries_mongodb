import matplotlib.pyplot as plt
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
        {"$sort": {"total": -1}},  # Ordena os resultados em ordem decrescente
        {"$limit": 6}  # Limita aos 6 primeiros idiomas
    ]
    resultado_agregacao = colecao.aggregate(pipeline)

    # Extrai os resultados da agregação
    idiomas = []
    total_ocorrencias = []
    for documento in resultado_agregacao:
        idiomas.append(documento["_id"])
        total_ocorrencias.append(documento["total"])

    # Plotagem do gráfico de barras
    plt.figure(figsize=(10, 6))
    plt.bar(idiomas, total_ocorrencias, color='skyblue')
    plt.xlabel('Idiomas')
    plt.ylabel('Total de Ocorrências')
    plt.title('Os 6 Idiomas Mais Falados')
    plt.xticks(rotation=45)  # Rotaciona os rótulos do eixo x para facilitar a leitura
    plt.tight_layout()
    plt.show()

except Exception as error:
    print("Erro ao plotar o gráfico de barras:", error)

cliente.close()
