# Flask AI EDA Agent

A lightweight end-to-end AI-assisted data exploration Flask app.

## Features
- Upload CSV datasets
- Automatic EDA using Pandas + NumPy
- AI-style insight generation
- Auto-generated plots using Matplotlib and Seaborn
- Clean, minimal architecture
- Ready for Docker, Gunicorn, Render, or Heroku deployment

## Run Locally
pip install -r requirements.txt
python app.py


## Deploy with Docker

docker build -t flask-eda .
docker run -p 5000:5000 flask-eda