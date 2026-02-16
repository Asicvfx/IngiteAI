# 🚀 IngiteAI Quickstart Guide

Follow these steps to launch the futuristic Lead Intelligence Dashboard.

## 1. Backend Setup (Django + Daphne)
The backend handles AI logic, database, and real-time WebSockets.

1.  **Open a Terminal** in the `backend` directory:
    ```cmd
    cd backend
    ```
2.  **Activate Virtual Environment**:
    ```cmd
    venv\Scripts\activate.bat
    ```
3.  **Install Dependencies**:
    ```powershell
    pip install -r requirements.txt
    ```
4.  **Configure Environment**:
    Make sure your `.env` file has your `OPENAI_API_KEY`.
5.  **Run Migrations**:
    ```powershell
    python manage.py migrate
    ```
6.  **Start the Server (Daphne for WebSockets)**:
    ```powershell
    daphne -p 8000 config.asgi:application
    ```

---

## 2. Frontend Setup (Nuxt.js)
The frontend is the premium user interface.

1.  **Open a New Terminal** in the `frontend` directory:
    ```powershell
    cd frontend
    ```
2.  **Install Dependencies**:
    ```powershell
    npm install
    ```
3.  **Launch Dev Server**:
    ```powershell
    npm run dev
    ```
4.  **Access the Dashboard**:
    Open [http://localhost:3000](http://localhost:3000) in your browser.

---

## 3. Neural Sync (Real-time)
The system uses **Daphne** to support real-time lead updates. If you see "WebSocket connected" in the browser console, the neural sync is active.

**Admin Credentials**:
You can create a superuser to access the admin panel at `http://localhost:8000/admin`:
```powershell
python manage.py createsuperuser
```
