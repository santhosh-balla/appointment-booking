# Appointment Booking System

## 💡 Description
This is a Django-based web application designed for small businesses to manage appointments with their clients. It supports company and customer logins, appointment scheduling, and a calendar interface similar to Google Calendar.

## 🚀 Features
- Company and customer registration/login
- Schedule and view appointments
- Calendar interface for intuitive scheduling
- Email/SMS notifications (mocked or optional)
- Clean and simple UI

## ⚙️ Requirements
- Python 3.10+
- pip
- SQLite (included by default)
- Virtualenv (recommended)

## 🛠️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/appointment-booking.git
   cd appointment-booking
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

6. **(Optional) Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Login Credentials (Optional for Testing)**
   ```
   Company:
   Email: test@company.com
   Password: testpass123

   Customer:
   Email: test@customer.com
   Password: testpass123
   ```

## 📝 Notes
- The app uses SQLite for easy setup.
- Email/SMS notifications are mocked or disabled for local development.

## 📂 File Structure Overview
- `appointments/`: Main Django app for handling scheduling logic
- `users/`: Handles registration and authentication
- `templates/`: Contains HTML templates
- `static/`: CSS and static files
- `db.sqlite3`: Default SQLite database
- `requirements.txt`: Python dependencies

## 📄 License
MIT License (or specify your own)
