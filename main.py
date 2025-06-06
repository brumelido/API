from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI(
    title="Minha API Documentada com Swagger",
    description="Uma API simples com dois endpoints usando FastAPI e Swagger UI.",
    version="1.0.0"
)

@app.get("/")
def home():
    """
    Rota raiz

    - Exibe uma mensagem de boas-vindas e sugere acessar a documentação.
    """
    return {"mensagem": "API no ar! Visite /docs para ver a documentação."}

@app.get("/hello")
def read_root(name: Optional[str] = Query(None, description="Nome da pessoa para cumprimentar")):
    """
    Endpoint

    - **name**: Nome para personalizar a mensagem
    - Retorna uma mensagem
    """
    if name:
        return {"message": f"Olá, {name}!"}
    return {"message": "Olá, mundo!"}

@app.get("/sum")
def sum_numbers(a: float = Query(..., description="Primeiro número"), b: float = Query(..., description="Segundo número")):
    """
    Soma dois números

    - **a**: Primeiro número (obrigatório)
    - **b**: Segundo número (obrigatório)
    - Retorna o resultado da soma
    """
    return {"resultado": a + b}
