#  Finance Dashboard Backend

A backend system for managing financial records with role-based access control and dashboard analytics. Built using Django and Django REST Framework.

##  Features

- **User & Role Management**  
  Custom user roles (Viewer, Analyst, Admin) with role-based access control.

- **Financial Records Management**  
  CRUD operations for income and expense records with fields like amount, category, date, and notes.

- **Filtering Support**  
  Filter records by type, category, and date.

- **Dashboard APIs**  
  Provides summary data such as total income, expenses, net balance, category-wise totals, recent activity, and monthly trends.

- **Access Control**  
  Backend-level restrictions based on user roles to control actions.

- **Validation & Error Handling**  
  Ensures valid input data and returns proper error messages with appropriate status codes.
## 🛠️ Tech Stack

* Python
* Django
* Django REST Framework
* SQLite (default)

---

## 📁 Project Structure

```
finance_backend/
│
├── users/
│   ├── models.py
│   ├── views.py
│   ├── api.py (serializers)
│   ├── permission.py
│   ├── urls.py
│
├── finance_backend/
│   ├── settings.py
│   ├── urls.py
│
├── manage.py
```

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```
git clone https://github.com/your-username/finance-dashboard-backend.git
cd finance-dashboard-backend
```

### 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Run Migrations

```
python manage.py makemigrations
python manage.py migrate
```

### 4. Create Superuser

```
python manage.py createsuperuser
```

### 5. Run Server

```
python manage.py runserver
```

---

## 🔗 API Endpoints

### User APIs

* `/api/users/`

### Financial Records

* `/api/records/`

### Dashboard APIs

* `/api/records/summary/`
* `/api/records/category_summary/`
* `/api/records/recent/`
* `/api/records/monthly/`

---

## 🧠 Design Highlights

* Clean separation of concerns (models, serializers, views)
* Role-based access control using custom permissions
* Efficient aggregation using Django ORM (`Sum`, `annotate`)
* Scalable API structure using DRF ViewSets

---

## 🎯 Conclusion

This project demonstrates backend development concepts including:

* REST API design
* Role-based authorization
* Data aggregation
* Validation and error handling
---
