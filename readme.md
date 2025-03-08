# Spam Identifier REST API

This project implements a REST API for identifying spam phone numbers, managing contacts, and searching users by phone number or name. The API is designed to be consumed by a mobile app, with robust security and scalability.

---

## Features
1. **User Management**:
   - Register users with unique phone numbers.
   - Authenticate users using JWT tokens.

2. **Spam Detection**:
   - Mark any phone number as spam.
   - Track the spam likelihood of phone numbers globally.

3. **Search Functionality**:
   - Search by name or phone number.
   - Prioritized and flexible search results.

---

## Installation

### **Requirements**
- Python 3.10+
- pip (Python package installer)
- Virtual environment (optional but recommended)

### **Setup Instructions**
1. Copy this File

   cd spam_identifier

2. Set Up a Virtual Environment (Optional but recommended):

    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies:

    pip install -r requirements.txt

4. Run Migrations:

    python manage.py makemigrations
    python manage.py migrate

5. Create a Superuser:

    python manage.py createsuperuser

6. Populate Sample Data: Run the custom management command to populate the database with sample data:

    python manage.py populate_sample_data

7. Start the Development Server:

    python manage.py runserver


Usage
API Endpoints
The base URL for all endpoints is http://127.0.0.1:8000/api/.

1. Register User
    URL: /register/
    Method: POST
    Request Body:
    
    {
        "username": "testuser",
        "phone_number": "1234567890",
        "password": "password123"
    }
    Response:
   
    {
        "id": 1,
        "username": "testuser",
        "phone_number": "1234567890"
    }
2. Obtain JWT Token
    URL: /token/
    Method: POST
    Request Body:
    
   
    {
        "username": "testuser",
        "password": "password123"
    }
    Response:
    
    
    {
        "access": "<access_token>",
        "refresh": "<refresh_token>"
    }
3. Mark a Number as Spam
    URL: /mark-spam/
    Method: POST
    Headers:
    http
    Authorization: Bearer <access_token>
    Request Body:
    {
        "phone_number": "9876543210"
    }

    Response:
    {
        "message": "Number marked as spam",
        "spam_count": 4
    }
4. Search by Name or Phone Number
    URL: /search/
    Method: GET
    Headers:
    http
    Authorization: Bearer <access_token>
    Query Parameters: ?query=<search_term>
    Response (Name Search):

    [
        {
            "name": "testuser",
            "phone_number": "1234567890"
        }
    ]
    Response (Phone Number Search):
    
    [
        {
            "phone_number": "9876543210",
            "spam_count": 4
        }
    ]
