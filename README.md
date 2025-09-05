# 🩺 Health Check Service

A Django-based health monitoring service that tracks the status of external endpoints and exposes metrics via a REST API.

---

## 🚀 Overview

This service provides a robust health checking system that monitors multiple external endpoints and exposes their status through a clean API interface. It's built with Django REST Framework for reliability and scalability.

---

## ✨ Features

- **Endpoint Monitoring**: Continuously checks the health of configured external services.
- **REST API**: Exposes health metrics via `/health/` endpoint with detailed status information.
- **Historical Data**: Maintains a history of health check results for analysis.
- **Admin Interface**: Django admin support for easy management of endpoints.
- **Configurable**: Easy to set up and customize for different environments.

---

## 🛠️ Installation

Clone the repository:

```bash
git clone https://github.com/samobeng14Dev/health-check-service
cd health_check_service

---

## Intall dependencies:
pip install -r requirements.txt

## Apply migration
python manage.py migrate

## Create a superuser account:
python manage.py createsuperuser

## Run development server
python manage.py runserver

---

##⚙️ Configuration
Access the Swagger UI at http://localhost:8000/
## 🔐 Admin Access

To access the Django admin panel:
open python shell -- python manage.py shell

1. Run `python manage.py createsuperuser` and complete the steps
2. Visit `http://127.0.0.1:8000/admin/`
3. Log in with your credentials


Add endpoints to monitor in the Endpoints section.

Configure each endpoint with a name and URL.

## 📡 API Usage
GET http://127.0.0.1:8000/health/v1/health/

# Response
{
  "summary": {
    "total_endpoints": 3,
    "up_endpoints": 2,
    "down_endpoints": 1,
    "timestamp": "2023-10-05T12:34:56.789Z"
  },
  "results": [
    {
      "id": 1,
      "endpoint": {
        "id": 1,
        "name": "Example Service",
        "url": "https://api.example.com/health",
        "is_active": true,
        "created_at": "2023-10-05T12:00:00.000Z",
        "updated_at": "2023-10-05T12:00:00.000Z"
      },
      "status_code": 200,
      "response_time": 0.45,
      "is_up": true,
      "error_message": null,
      "checked_at": "2023-10-05T12:34:56.789Z"
    }
  ]
}



