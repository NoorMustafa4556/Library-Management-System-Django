# Library Management System (LMS) using Django

This repository contains the source code for a fully functional Library Management System (LMS) developed using the Django framework. The project demonstrates core Django concepts such as MVT architecture, ORM, user authentication, and admin panel customization. It features a clean, responsive user interface for browsing and requesting books, and a powerful backend for administrators to manage the entire library inventory and user requests efficiently.

---


## 📸 Project Screenshots

<p align="center">
  <img src="https://raw.githubusercontent.com/NoorMustafa4556/Library-Management-System-Django-/main/myproject/myapp/static/images/1.jpg" alt="Screenshot 1" width="30%" />
  <img src="https://raw.githubusercontent.com/NoorMustafa4556/Library-Management-System-Django-/main/myproject/myapp/static/images/2.jpg" alt="Screenshot 2" width="30%" />
  <img src="https://raw.githubusercontent.com/NoorMustafa4556/Library-Management-System-Django-/main/myproject/myapp/static/images/3.jpg" alt="Screenshot 3" width="30%" />
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/NoorMustafa4556/Library-Management-System-Django-/main/myproject/myapp/static/images/4.jpg" alt="Screenshot 4" width="30%" />
  <img src="https://raw.githubusercontent.com/NoorMustafa4556/Library-Management-System-Django-/main/myproject/myapp/static/images/5.jpg" alt="Screenshot 5" width="30%" />
  <img src="https://raw.githubusercontent.com/NoorMustafa4556/Library-Management-System-Django-/main/myproject/myapp/static/images/6.jpg" alt="Screenshot 6" width="30%" />
</p>



## Features

### For Users (Library Members)
- **User Authentication:** Secure signup and login system for members.
- **Browse Catalogue:** A beautiful home page to view all available books with images and details.
- **Category Filtering:** Filter books by specific categories (e.g., Computer Science, Biology).
- **Advanced Search:** A powerful search bar to find books by title or category.
- **Book Request System:** Logged-in users can request a book with a single click.
- **Request Status:** A dedicated "My Requests" page to track the status (Pending, Approved, Rejected) of all requests.

### For Administrators
- **Admin Panel:** Full control via the customized Django Admin Panel.
- **Inventory Management:** Easily add, update, or delete books, authors, and categories.
- **Request Approval System:** A streamlined interface to view all user requests and approve or reject them.

---

## Tech Stack
- **Backend:** Python, Django
- **Frontend:** HTML, CSS, Bootstrap 5
- **Database:** SQLite3 (Default)

---



## How to Download and Use (Setup Instructions)

To get a local copy up and running, follow these simple steps.

### Prerequisites
- Python 3.8 or higher
- Git

### Installation Steps

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/NoorMustafa4556/Library-Management-System-Django-.git
    ```

2.  **Navigate to the main project directory:**
    ```bash
    cd Library-Management-System-Django-
    ```

3.  **Create and activate a virtual environment:**
    ```bash
    # Create venv
    python -m venv Venv

    # Activate on Windows
    Venv\Scripts\activate
    ```

4.  **Navigate into the Django project folder (where manage.py is):**
    ```bash
    cd myproject
    ```

5.  **Install the required dependencies:**
    (This will install Django, Pillow, etc.)
    ```bash
    pip install -r requirements.txt
    ```

6.  **Apply database migrations:**
    (This will create the database tables for our models)
    ```bash
    python manage.py migrate
    ```

7.  **Create a superuser to access the admin panel:**
    (Follow the prompts to create an admin account)
    ```bash
    python manage.py createsuperuser
    ```

8.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

### How to Use the Application

1.  **Admin Side:**
    -   Go to `http://127.0.0.1:8000/admin/`
    -   Log in with the superuser credentials you created.
    -   Here you can add new categories, books, and manage user requests.

2.  **User Side:**
    -   Go to `http://127.0.0.1:8000/`
    -   Create a new account using the "Sign Up" button.
    -   Log in with your new account.
    -   You can now browse books, filter by category, and request any book you like!


---
