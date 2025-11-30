# 🚀 Real-Time Pair Programming Web Application  
**FastAPI Backend + WebSockets + JSON Storage + React (JavaScript) Frontend**  
**Includes Makefile for Easy Setup**

---

## 📌 Overview  
This project is a fully functional **real-time pair programming prototype**.  
It allows multiple users to join a shared room and collaborate on code instantly.

### Features include:
- FastAPI backend (Python)
- WebSockets for live collaboration
- JSON file storage (no DB)
- React JS UI
- Modern designer UI
- Mock AI autocomplete suggestions

---

## 📁 Folder Structure
```
project/
├── backend/
│   ├── Makefile
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
    │   ├── main.jsx
    │   └── index.css
    └── public/
```

---

# ⚙️ Running the Project (Makefile)

## 🟣 Backend Setup (FastAPI)

### 1. Create Virtual Environment
```
make backend-venv
```

### 2. Activate Virtual Environment
Mac/Linux:
```
source backend/venv/bin/activate
```
Windows:
```
backend\venv\Scripts\activate
```

### 3. Install Dependencies
```
make install-backend
```

### 4. Run Backend Server
```
make run-backend
```

---

## 🟡 Frontend Setup (React JS)

Open another terminal window:

### 1. Install Dependencies
```
make install-frontend
```

### 2. Run Frontend UI
```
make run-frontend
```

Frontend runs at:  
👉 http://localhost:3000

Backend runs at:  
👉 http://localhost:8000  
👉 WebSocket: ws://localhost:8000/ws/{roomId}

---

# 🔌 API Endpoints

### **POST /rooms**
Creates a new collaboration room.

### **POST /autocomplete**
Returns a mocked AI suggestion.

### **WebSocket /ws/{roomId}**
Supports:
```
{ "type": "edit", "code": "..." }
{ "type": "cursor", "cursor": {...} }
```

---

# 🛠 Tech Stack

### Backend
- Python 3.x  
- FastAPI  
- WebSockets  
- JSON file storage  

### Frontend
- React  
- JavaScript  
- CSS  

---

# 🚧 Limitations
- JSON file not suitable for production  
- No authentication  
- Last-write-wins sync  
- No multi-server scaling  

---

# 🚀 Future Improvements
- Replace textarea → Monaco Editor  
- Add authentication  
- Add file explorer  
- Database support  
- Real AI autocomplete  

---

# 🎉 Status
Project is fully functional as a real-time collaboration prototype.
