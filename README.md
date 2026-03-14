# Mock Interview Platform

The **Mock Interview Platform** is a full-stack web application designed to help B.Tech students practice and perfect their technical and behavioral interviewing skills. It simulates a realistic interview environment, evaluating candidates on their technical depth, problem-solving approach, and communication clarity.

## 🚀 Features

*   **Interactive HUD Interface:** A modern, immersive UI featuring an AI visualizer, dynamic progress tracking, and split-pane coding environments.
*   **Voice Interaction:** Built-in Web Speech API integration for hands-free, realistic vocal interactions with the AI interviewer.
*   **Intelligent Code Evaluator:** A secure, test-driven Python execution engine that evaluates code submissions based on logic and correctness, rather than rigid string matching. Includes a full code editor with highlighting.
*   **Concept-Based Evaluation:** Advanced evaluation algorithms that grade candidates on *concepts* ("own words" recognition) rather than strict textbook keywords.
*   **Recruiter's Scorecard:** Professional post-interview feedback featuring a Hiring Decision (Strong Hire, Hire, Leaning No, No Hire), evidence-based logs, and detailed scores across three core pillars:
    *   *Technical Depth*
    *   *Problem Solving*
    *   *Communication*

## 🛠️ Tech Stack

*   **Frontend:** Vanilla HTML5, CSS3 (Custom Glassmorphism Design System), JavaScript.
*   **Backend:** Python 3, Flask, Gunicorn.
*   **Database:** SQLite3 (`interview.db`).
*   **AI Engine:** Custom local heuristic and Natural Language Processing (NLP) rules for question generation and concept-based grading (no external API keys required).

## 💻 Running Locally

### Prerequisites
*   Python 3.10+

### Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd mock-interview
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your environment variables (e.g., in a `.env` file):
   ```
   FLASK_SECRET_KEY=your_secret_key
   ```

### Execution
Start the Flask backend (which also automatically serves the frontend):
```bash
python backend/app.py
```
Open your browser and navigate to `http://127.0.0.1:5000` to access the application.

## ☁️ Deployment

This application is configured for seamless deployment on cloud providers like Render or Heroku. It utilizes a `Procfile` and `gunicorn` to serve the full-stack application securely.

```bash
# Example Procfile
web: gunicorn --chdir backend --bind 0.0.0.0:$PORT app:app
```
