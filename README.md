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
# 👋 Hi, I'm Noor Mustafa

A passionate and results-driven **Flutter Developer** from **Bahawalpur, Pakistan**, specializing in building elegant, scalable, and high-performance cross-platform mobile applications using **Flutter** and **Dart**.

With a strong understanding of **UI/UX principles**, **state management**, and **API integration**, I aim to deliver apps that are not only functional but also user-centric and visually compelling. My development approach emphasizes clean code, reusability, and performance.

---

## 🚀 What I Do

- 🧑‍💻 **Flutter App Development** – I build cross-platform apps for Android, iOS, and the web using Flutter.
- 🔗 **API Integration** – I connect apps to powerful RESTful APIs and third-party services.
- 🎨 **UI/UX Design** – I craft responsive and animated interfaces that elevate the user experience.
- 🔐 **Authentication & Firebase** – I implement secure login systems and integrate Firebase services.
- ⚙️ **State Management** – I use Provider, setState, and Riverpod (in-progress) for scalable app architecture.
- 🧠 **Clean Architecture** – I follow MVVM and MVC patterns for maintainable code.

---


## 🌟 Projects I'm Proud Of

- 🌤️ **[Live Weather Check App](https://github.com/NoorMustafa4556/Live-Weather-Check-App)** – Real-time weather forecast using OpenWeatherMap API  
- 🤖 **[AI Chatbot (Gemini)](https://github.com/NoorMustafa4556/Ai-ChatBot)** – Conversational AI chatbot powered by Google’s Gemini  

- 🍔 **[Recipe App](https://github.com/NoorMustafa4556/Recipe-App)** – Discover recipes with images, categories, and step-by-step instructions  

- 📚 **[Palindrome Checker](https://github.com/NoorMustafa4556/Palindrome-Checker-App)** – A Theory of Automata-based project to identify palindromic strings  

> 🎯 Check out all my repositories on [github.com/NoorMustafa4556](https://github.com/NoorMustafa4556?tab=repositories)

---

## 🛠️ Tech Stack & Tools

| Area                | Tools/Technologies |
|---------------------|--------------------|
| **Languages**       | Dart, JavaScript, Python (basic) |
| **Mobile Framework**| Flutter            |
| **Backend/Cloud**   | Firebase (Auth, Realtime DB, Storage), Django, Flask |
| **Frontend (Web)**  | React.js (basic), HTML, CSS, Bootstrap |
| **State Management**| Provider, setState, Riverpod (learning) |
| **API & Storage**   | REST APIs, HTTP, Shared Preferences, SQLite |
| **Design**          | Material, Cupertino, Lottie Animations, Gradient UI |
| **Version Control** | Git, GitHub        |
| **Tools**           | Android Studio, VS Code, Postman, Figma (basic) |

---

## 🧰 Tech Toolbox

<p align="left">
  <img src="https://img.shields.io/badge/Dart-0175C2?style=for-the-badge&logo=dart&logoColor=white"/>
  <img src="https://img.shields.io/badge/Flutter-02569B?style=for-the-badge&logo=flutter&logoColor=white"/>
  <img src="https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge&logo=firebase&logoColor=black"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white"/>
  <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB"/>
  <img src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white"/>
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white"/>
</p>

---

## 📈 Current Focus

- 💡 Enhancing Flutter animations and transitions
- 🤖 Implementing AI-based logic with Google Gemini API
- 📲 Building portfolio-level applications using full-stack Django & Flutter

---

## 📫 Let's Connect!

<p align="left">
  <a href="https://x.com/NoorMustafa4556" target="blank">
    <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="X / Twitter" height="30" width="40" />
  </a>
  <a href="https://www.linkedin.com/in/noormustafa4556/" target="blank">
    <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="LinkedIn" height="30" width="40" />
  </a>
  <a href="https://www.facebook.com/NoorMustafa4556" target="blank">
    <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/facebook.svg" alt="Facebook" height="30" width="40" />
  </a>
  <a href="https://instagram.com/noormustafa4556" target="blank">
    <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="Instagram" height="30" width="40" />
  </a>
  <a href="https://wa.me/923087655076" target="blank">
    <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/whatsapp.svg" alt="WhatsApp" height="30" width="40" />
  </a>
  <a href="https://www.tiktok.com/@noormustafa4556" target="blank">
    <img src="https://cdn-icons-png.flaticon.com/512/3046/3046122.png" alt="TikTok" height="30" width="30" />
  </a>
</p>

- 📍 **Location:** Bahawalpur, Punjab, Pakistan

---

> _“Learning never stops. Every app I build makes me a better developer — one widget at a time.”_

---

