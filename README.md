# 🛒 Fast Shopping List API

**Clean, production-ready REST API built with FastAPI, Pydantic v2, and Docker**

A backend-focused project demonstrating practical software engineering skills, clean architecture, and DevOps-oriented thinking. Designed to be easily readable, testable, and deployable.

---

## ⚡ 30-Second Overview (For Recruiters)

* **What it is:** A RESTful CRUD API for managing shopping items
* **Why it matters:** Demonstrates clean backend architecture, validation, and containerization
* **Key skills shown:** FastAPI, Pydantic, Docker, modular design, API documentation
* **Production mindset:** Stateless design, clear separation of concerns, Docker-ready

---

## 🚀 Key Features

* **CRUD Operations** – Create, read, update, and delete items
* **Category Filtering** – Enum-based filtering (dairy, vegetables, dry goods, etc.)
* **Strong Validation** – Pydantic schemas enforce data correctness
* **Auto-Generated Docs** – Interactive Swagger UI
* **Containerized** – Ready for local or Docker-based execution

---

## 🧠 Architecture Highlights

* **Modular / Layered Design**

  * API routes
  * Data models (Pydantic & Enums)
  * Data access layer (in-memory storage)
* **Stateless API** – Easy to scale or connect to a real database
* **Clean Code Principles** – Clear responsibilities, minimal logic in routes

---

## 🛠 Tech Stack

* **Python 3.11+**
* **FastAPI**
* **Pydantic v2**
* **Docker**
* **python-dotenv**

---

## 📁 Project Structure

```text
Fast_Shopping_list/
├── src/
│   ├── main.py          # API routes
│   ├── models.py        # Schemas and Enums
│   └── database.py      # In-memory data layer
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## ⚙️ Run Locally

```bash
python -m venv .venv
source .venv/Scripts/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cd src
fastapi dev main.py
```

API available at: `http://localhost:8000`

---

## 🐳 Run with Docker

```bash
docker build -t fast-shopping-list .
docker run -p 8000:8000 fast-shopping-list
```

---

## 📖 API Documentation

* Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
* OpenAPI Spec: [http://localhost:8000/openapi.json](http://localhost:8000/openapi.json)

---

## 🔮 Next Steps

* Replace in-memory storage with PostgreSQL
* Add authentication (JWT)
* Add automated tests (Pytest)
* CI/CD with GitHub Actions

---

## 👨‍💻 Author

Idan Rodriguez
B.Sc. Computer Science Graduate | Backend / Cloud-Oriented Developer
