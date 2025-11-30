# 🚀 Real-Time Pair Programming Web App  
FastAPI (Backend) + WebSockets + JSON Storage + React JS UI

This project is a simplified real-time pair programming web application where two users can:
- Join the same room
- Edit code simultaneously
- See updates instantly via WebSockets
- Receive AI-style mocked autocomplete suggestions

Backend uses FastAPI, WebSockets, and a JSON file instead of a database.  
Frontend is built with React (JavaScript).

## ⭐ Features
- Real-time collaboration
- WebSocket-based live sync
- Mocked AI autocomplete
- JSON file storage
- Modern styled UI

## 📁 Project Structure
project/
├── backend/
│   ├── requirements.txt
│   ├── rooms.json
│   └── app/
│       ├── main.py
│       ├── storage.py
│       ├── ws_manager.py
│       ├── schemas.py
│       ├── routers/
│       │   ├── rooms.py
│       │   └── autocomplete.py
│       └── services/
│           └── __init__.py
└── frontend/
    ├── package.json
    ├── src/
    │   ├── App.js
    │   ├── App.css
    │   └── main.jsx
    └── public/

## ⚙️ Installation & Running Guide

### Backend (FastAPI)
1. Create virtual environment  
Mac/Linux:
```
python3 -m venv venv
```
Windows:
```
python -m venv venv
```

2. Activate environment  
Mac/Linux:
```
source venv/bin/activate
```
Windows:
```
venv\Scripts\activate
```

3. Install requirements:
```
pip install -r requirements.txt
```

4. Run backend:
```
cd backend/app
python3 main.py
```

### Frontend (React)
Open new terminal:

1. Navigate to frontend:
```
cd frontend
```

2. Install dependencies:
```
npm install
```

3. Run UI:
```
npm start
```

## 🔌 API Endpoints
### POST /rooms
Creates a new room.

### POST /autocomplete
Returns mocked AI suggestions.

### WebSocket /ws/{roomId}
Handles real-time code synchronization.

## 🛠️ Tech Stack
- FastAPI
- WebSockets
- React JS
- JSON File Storage

## 🚧 Limitations
- Not designed for multi-node scaling
- No authentication
- Simple last-write-wins model

## 🚀 Future Improvements
- Monaco editor
- Authentication
- File tree support
- Database integration

