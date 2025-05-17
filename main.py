from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI(
    title="Minha API Documentada com Swagger",
    description="Uma API simples com dois endpoints usando FastAPI e Swagger UI.",
    version="1.0.0"
)

@app.get("/hello")
def read_root(name: Optional[str] = Query(None, description="Nome da pessoa para cumprimentar")):
    """
    Endpoint de saudação

    - **name**: Nome opcional para personalizar a mensagem
    - Retorna uma mensagem de saudação
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