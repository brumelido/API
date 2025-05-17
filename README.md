# 🚀 Minha API Documentada com Swagger

Essa é uma API REST simples desenvolvida com **FastAPI**, documentada automaticamente com **Swagger UI** e publicada na nuvem usando a **Render**.

## 🌐 Link da API
- **Home:** [https://api-49h9.onrender.com/](https://api-49h9.onrender.com/)
- **Swagger UI (Documentação):** [https://api-49h9.onrender.com/docs](https://api-49h9.onrender.com/docs)
- **Redoc:** [https://api-49h9.onrender.com/redoc](https://api-49h9.onrender.com/redoc)

## 📦 Endpoints disponíveis

| Método | Rota        | Descrição                                           | Parâmetros                           |
|--------|-------------|-----------------------------------------------------|--------------------------------------|
| GET    | `/`         | Mensagem de boas-vindas                             | —                                    |
| GET    | `/hello`    | Retorna uma saudação personalizada ou padrão        | `name` (opcional)                    |
| GET    | `/sum`      | Soma dois números e retorna o resultado             | `a` (obrigatório), `b` (obrigatório) |

---

## 📁 Estrutura do Projeto

```
📦 CassebAPI/
├── main.py
├── requirements.txt
└── start.sh
```

---

## 🚀 Como rodar localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repo.git
   cd seu-repo
   ```

2. Crie um ambiente virtual e ative:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Rode o servidor:
   ```bash
   uvicorn main:app --reload
   ```

---

## ☁️ Deploy com Render

A API foi publicada usando a plataforma [Render](https://render.com), conectando diretamente ao repositório do GitHub. O comando de inicialização configurado foi:

```bash
uvicorn main:app --host 0.0.0.0 --port 10000
```

---

## 📚 Tecnologias usadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [Swagger UI](https://swagger.io/tools/swagger-ui/)
- [Render](https://render.com/)

---

## ✨ Autora

Feita com ❤️ por **Bruna Melido**
