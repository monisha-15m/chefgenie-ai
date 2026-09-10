# ChefGenie AI

ChefGenie is a specialised recipe chatbot built with:

- Python
- Flask
- Google Gemini API
- HTML/CSS/JavaScript
- Gunicorn
- Render

## Project structure

ChefGenie/
├── app.py
├── chatbot_config.py
├── requirements.txt
├── .env
├── .gitignore
├── render.yaml
├── README.md
└── templates/
    └── index.html

## Local setup

1. Open the project folder in VS Code.
2. Put your Gemini API key in `.env`.
3. Install dependencies:
   `pip install -r requirements.txt`
4. Run:
   `python app.py`
5. Open:
   `http://127.0.0.1:5000`

## Render deployment

Build Command:
`pip install -r requirements.txt`

Start Command:
`gunicorn app:app`

Environment Variables:
- GEMINI_API_KEY = your real Gemini API key
- GEMINI_MODEL = gemini-3.5-flash-lite

Do not upload `.env` to GitHub.

## Health check

After deployment, open:
`https://YOUR-RENDER-SERVICE.onrender.com/health`

Expected response:
`{"service":"ChefGenie","status":"ok"}`
