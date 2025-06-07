🧾 AuctionCRM Backend
Django REST API for a full-stack CRUD learning project — client and auction item management.

🔍 Overview
This repo provides the backend for AuctionCRM, a full-stack CRUD application built to practice integration between React and Django REST Framework. The API supports client and inventory management features, with endpoints designed for hands-on learning and scalable architecture.

⚙️ Features
🔁 RESTful Endpoints for Clients and Auction Items

🧩 JSONField model support for flexible data storage

🌐 CORS Enabled to support React frontend integration

🔐 Placeholder for authentication (ready for JWT or session setup)

⚙️ Modular Django App Structure for easy feature expansion

🧰 Tech Stack
Framework: Django 3.2.12

API Toolkit: Django REST Framework 3.12.4

Cross-Origin Support: django-cors-headers 3.7.0

Dynamic Fields: jsonfield 3.1.0

Database: SQLite (default) or switchable to PostgreSQL

🚀 Getting Started
1. Clone & Install
bash
git clone https://github.com/AshB4/BackendForCrm.git  
cd BackendForCrm  
pip install -r requirements.txt  
2. Run the Development Server
bash
python manage.py runserver
The API will be available at http://localhost:8000

📁 Example Endpoints
Method	Endpoint	Description
GET	/api/clients/	List all clients
POST	/api/clients/	Create a new client
GET	/api/items/	List all auction items
POST	/api/items/	Add a new item

Full CRUD available for both clients and items. Swagger or Postman collection available upon request.

🔗 Connect to Frontend
Use this repo with the frontend:
👉 AuctionCRM Frontend (React)

📌 Project Status
✔️ Active — used as a training sandbox
🔜 Future goals:

Add authentication (JWT/session)

Pagination, filtering, and search

Swagger/OpenAPI docs

📄 License
MIT License
