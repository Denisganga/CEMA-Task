# Health Information System

This project is a basic **Health Information System** built with **Django (DRF)** for the backend and **React** for the frontend. It allows doctors (system users) to manage health programs, register clients, enroll clients into programs, and view client profiles via a RESTful API.

---

## Features

- Create Health Programs (e.g., TB, Malaria, HIV)
- Register New Clients
- Enroll Clients in Programs
- Search and View Client Profiles
- Expose Client Profiles through RESTful APIs
- Clean, structured, and scalable codebase

---

## Technologies Used

- **Backend:** Django, Django REST Framework (DRF)
- **Frontend:** React.js
- **Authentication:** JWT Authentication
- **Database:** SQLite (for development)

---

## Getting Started

### Backend Setup (Django)

1. **Clone the Repository**

```bash
git clone https://github.com/denisganga/CEMA-Task.git
cd health_system
```

2. **Create Virtual Environment and Activate**

```bash
python -m venv myenv
source myenv/bin/activate    # Linux/macOS
myenv\Scripts\activate       # Windows
```

3. **Install Backend Requirements**

```bash
pip install -r requirements.txt
```

4. **Run Migrations**

```bash
python manage.py migrate
```
JWT Authentication (Login create superuser)
  ```bash
  python manage.py createsuperuser
  ```
5. **Start Django Server**

```bash
python manage.py runserver
```

Backend will run at:  
`http://127.0.0.1:8000/`

---

### Frontend Setup (React)

1. **Navigate to Frontend Folder**

```bash
cd ../frontend
```

2. **Install Frontend Dependencies**

```bash
npm install
```

3. **Start React Development Server**

```bash
npm start
```

Frontend will run at:  
`http://localhost:3000/`

---

## Important API Endpoints

| Method | Endpoint | Description |
|:-------|:---------|:------------|
| POST | `/clients/add_program/` | Add a new health program |
| POST | `/clients/register/` | Register a new client |
| POST | `/clients/enroll/` | Enroll a client in a program |
| GET | `/clients/enrollments/` | List all client enrollments |
| GET | `/clients/list/` | List all registered clients |

---

## Folder Structure

```
backend/
  ├── core/
  │    ├── models.py
  │    ├── serializers.py
  │    ├── views.py
  │    └── urls.py
  ├── manage.py
  └── settings.py
frontend/
  ├── src/
  │    ├── components/
  │    │     ├── EnrollClient.js
  │    │     ├── EnrolledClients.js
  │    │     └── RegisterClient.js
  │    ├── App.js
  │    └── index.js
  ├── package.json
  └── README.md
```

---


## Presentation & Prototype Demonstration

You can view the **PowerPoint presentation** and **prototype video demonstration** here:

🔗 [View Presentation & Demo](https://www.canva.com/design/DAGlwpwsr68/81XJ45Vpec3EKKV_q8j4sg/edit?utm_content=DAGlwpwsr68&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

_(The last slide contains the video demonstration!)_

---

## Author

**Denis**  
Software Engineering 

---

> **Note:**  
> Make sure both servers (backend + frontend) are running for full functionality!
