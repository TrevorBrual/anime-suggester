# Anime Suggestor 

A full-stack web application that helps users find their next anime to watch. Users can filter recommendations based on **Genre**, **Vibe** (e.g., Storytelling, Funny), and **Content Rating** (PG-13, R, etc.).

## Features
* **Recommendation Engine:** Filters a database of anime based on user preferences.
* **Multi-Select Filtering:** Users can select multiple content ratings (e.g., "PG-13" and "R") simultaneously.
* **Full-Stack Architecture:** * **Frontend:** Built with React for a dynamic, responsive user interface.
    * **Backend:** Powered by Python (Flask) to handle logic and data processing.
    * **API:** Custom REST API endpoints to fetch recommendations.

## Technologies Used
* **Frontend:** React.js, HTML5, CSS3
* **Backend:** Python 3, Flask
* **Tools:** VS Code, Git, GitHub

## How to Run This Project
Since this is a full-stack application, you need to run the Backend and Frontend in separate terminals.

### Prerequisites
* Node.js & npm installed
* Python installed

### Step 1: Start the Backend (Flask)
1.  Open a terminal and navigate to the backend folder:
    ```bash
    cd backend
    ```
2.  (Optional) Activate your virtual environment:
    * Windows: `.\venv\Scripts\activate`
    * Mac/Linux: `source venv/bin/activate`
3.  Install dependencies (if needed):
    ```bash
    pip install flask flask-cors
    ```
4.  Run the server:
    ```bash
    python app.py
    ```
    *The server will start on `http://127.0.0.1:5000`*

### Step 2: Start the Frontend (React)
1.  Open a **new** terminal (keep the backend running!) and navigate to the frontend folder:
    ```bash
    cd frontend
    ```
2.  Install dependencies (first time only):
    ```bash
    npm install
    ```
3.  Start the React app:
    ```bash
    npm start
    ```
    *The app will open in your browser at `http://localhost:3000`*

---
*Created by [Trevor Brual]*
