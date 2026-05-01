# PropspectAI

AI-powered commercial real estate prospecting tool built with Flask, React, and Tailwind CSS.

## What it does
- Search commercial property owners by city
- Surfaces aging landlords (20+ years of ownership) — the most motivated sellers
- Generates personalized AI cold call scripts using GPT-4 for each owner

## Tech Stack
- **Frontend:** React + Vite + Tailwind CSS
- **Backend:** Python + Flask
- **AI:** OpenAI GPT-4o-mini

## Running locally

### Backend
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py

### Frontend
cd frontend
npm install
npm run dev