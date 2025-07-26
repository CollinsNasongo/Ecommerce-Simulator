# 📊 E-Commerce Data Simulator

🚀 **A project to help users access real-time simulated e-commerce data for testing and development.**

---

## 📌 Project Overview
This tool generates **real-time e-commerce data** — including users, orders, products, and payments — and makes it accessible via a RESTful API. It is designed for developers, data engineers, and analysts who need **dynamic, realistic datasets** without relying on production systems.

---

## 🛠️ Technologies Used
- **🐍 Python:** Flask, SQLAlchemy, Faker  
- **🗃️ Database:** SQLite (local)  
- **📦 Docker:** Containerized environment  
- **📑 API Docs:** OpenAPI + Swagger UI  

---

## 📂 Project Structure
```
ecommerce-simulator/
├── app/
│   ├── models.py            # SQLAlchemy models
│   ├── routes.py            # API endpoints
│   ├── utils.py             # Data generation logic
│   ├── stream_simulator.py  # Streaming activity simulation
├── data/                    # SQLite database file
├── static/                  # openapi.yml for Swagger UI
├── templates/               # Swagger UI HTML (optional)
├── run.py                   # Flask entry point
├── Dockerfile               # Container setup
├── docker-compose.yml       # Service orchestration
└── requirements.txt         # Python dependencies
```

---

## 🚀 How to Use

### 1️⃣ Install Requirements
```bash
pip install -r requirements.txt
```

### 2️⃣ Initialize the Database
```bash
python run.py init_db
```

### 3️⃣ Run the Server
```bash
python run.py
```

### 4️⃣ Access Real-Time Data via API

- **Register a User**
  ```bash
  curl -X POST http://localhost:5000/users
  ```

- **Get All Users**
  ```bash
  curl http://localhost:5000/users
  ```

- **Simulate Streamed Activity**
  ```bash
  curl -X POST "http://localhost:5000/simulate_user_activity?max_events=10&interval_seconds=1"
  ```

---

## 📘 API Documentation

You can access the **interactive API docs** at:

🔗 [http://localhost:5000/swaggerui.html](http://localhost:5000/swaggerui.html)

Make sure:
- The `static/openapi.yml` file exists.
- The Swagger UI HTML correctly references it.

---

## ✅ Use Cases

- Testing ETL pipelines  
- API response testing  
- UI development without backend dependencies  
- Demo apps for analytics or dashboards  

---

## 🎯 Goal

This project aims to help users and developers **easily access real-time, evolving e-commerce data** without needing access to sensitive or live production systems.