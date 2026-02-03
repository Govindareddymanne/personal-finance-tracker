#  Personal Finance Tracker Application

The Personal Finance Tracker is a web-based application built using Flask and MySQL that helps users manage their daily income and expenses securely. It provides an easy way to track transactions, monitor balances, and maintain financial discipline.

---

##  Project Overview

This application allows users to create an account, log in securely, and manage their personal financial records. Users can add income and expense entries, categorize transactions, and view a real-time balance on their dashboard. All data is stored securely in a MySQL database and is accessible only to authenticated users.

---

##  Key Features

- User registration and secure login
- Password hashing for data security
- Session-based authentication
- Add income and expense transactions
- Category-wise transaction tracking
- Automatic balance calculation
- Transaction history displayed in dashboard
- Secure logout functionality

---

##  How It Works

1. Users register with their name, email, and password  
2. Passwords are encrypted using hashing before storage  
3. After login, users access a personal dashboard  
4. Income and expenses are recorded in the database  
5. The system calculates balance automatically  
6. Users can log out securely at any time  

---

##  Technology Stack

- **Backend:** Flask (Python)
- **Database:** MySQL
- **Frontend:** HTML, CSS, Jinja2 Templates
- **Security:** Werkzeug (password hashing)
- **Session Management:** Flask Sessions

---

##  Database Structure

### Users Table
- `id`
- `name`
- `email`
- `password`

### Transactions Table
- `id`
- `user_id`
- `amount`
- `category`
- `type` (income / expense)
- `created_at`

---

##  Installation & Execution

### 1️ Install Dependencies
```bash
pip install flask mysql-connector-python werkzeug# personal-finance-tracker
A Flask-based personal finance tracker that allows users to register, log in securely, track income and expenses, view transaction history, and monitor their balance using a MySQL database.
