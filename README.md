# 📊 E-Commerce Data Simulator

🚀 **Simulating real-time e-commerce data for practice and testing**  

## **📌 Project Overview**  
This project generates **realistic e-commerce data** in real time, including user registrations, purchases, and order details. The data is slightly modified on each iteration to simulate **live user activity and transactions**. It can be used for testing and development purposes, providing a dynamic dataset for e-commerce applications.  

---

## **🛠️ Technologies & Tools**  
- **🐍 Python** (Flask, SQLAlchemy, Faker)  
- **📂 Database:** SQLite  
- **📊 Data Generation:** Randomized user and purchase data  
- **📄 Data Storage:** SQL database for persistent data  

---

## **💽 Project Structure**  
```
📂 ECOMM
├── 🐜 README.md          # Project documentation
├── 📂 app                # Application source code
│   ├── __init__.py      # Initialization file
│   ├── database.py      # Database configuration
│   ├── models.py        # Database models
│   ├── routes.py        # API routes
│   └── utils.py         # Utility functions for data generation
├── 📂 data               # Data storage
├── 📂 instance           # Instance-specific files
│   ├── data.db          # SQLite database
│   └── config.py        # Configuration settings
├── 📜 requirements.txt   # Project dependencies
└── 📜 run.py             # Application entry point
```

---

## **🚀 How It Works**  
1. **Generate Fake Users:** Simulate user registrations with random details.  
2. **Simulate Purchases:** Create fake orders, order items, and payments for existing users.  
3. **Store Data:** Persist all generated data in an SQLite database.  
4. **API Access:** Retrieve and interact with data via a Flask API.  

---

## **⚡ Quick Start**  
### **1️⃣ Install Dependencies**  
```sh
pip install -r requirements.txt
```

### **2️⃣ Initialize the Database**  
```sh
python run.py init_db
```

### **3️⃣ Run the Application**  
```sh
python run.py
```

### **4️⃣ Generate Fake Data**  
- **Register a User:**  
  ```sh
  curl -X GET http://localhost:5000/register_user
  ```
- **Simulate a Purchase:**  
  ```sh
  curl -X GET http://localhost:5000/simulate_purchase
  ```

### **5️⃣ Access Data via API**  
- **Get All Users:**  
  ```sh
  curl -X GET http://localhost:5000/users
  ```
- **Get All Orders:**  
  ```sh
  curl -X GET http://localhost:5000/orders
  ```

---

## **📌 Future Improvements**  
✅ **Enhanced Data Realism:** Add more detailed user demographics and purchase patterns.  
✅ **Scalability:** Support for larger datasets and more complex transactions.  
✅ **Dockerized Deployment:** Simplify setup and deployment with Docker.  
✅ **Integration with External Services:** Connect to external APIs for real-time product data.  

---

This project provides a robust foundation for simulating e-commerce data, enabling developers to test and refine their applications with realistic, dynamic data.