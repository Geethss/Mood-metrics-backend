# Mood Metrics Backend

Mood Metrics is a sentiment analysis backend built using **FastAPI**. This backend processes text data from uploaded CSV files and performs sentiment analysis using the **VADER Sentiment Analyzer**. The backend is deployed on **Render**.

---

## Features

- Accepts CSV file uploads with a `text` column.
- Performs sentiment analysis (positive, negative, neutral).
- Returns sentiment scores and categories.
- Provides a summary of sentiment distribution.
- Includes Swagger UI documentation for testing endpoints.

---

## Live Demo

The backend API is deployed and accessible at:  
**[Mood Metrics Backend on Render](https://mood-metrics-backend.onrender.com/)**  

Explore the API documentation here:  
**[API Documentation](https://mood-metrics-backend.onrender.com/docs)**

---

## Installation

Follow these steps to set up the backend locally:

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

### Clone the Repository

git clone https://github.com/Geethss/Mood-metrics-backend.git
cd Mood-metrics-backend

### To install dependencies

pip install -r requirements.txt

Start the FastAPI server:

## To run the app locally

1. Use the command -
uvicorn app.main:app --reload

2. Open your browser and navigate to:

Swagger UI: http://127.0.0.1:8000/docs
Redoc: http://127.0.0.1:8000/redoc

### Endpoints

### /analyze - POST
Uploads a CSV file and performs sentiment analysis.

### Request
Content-Type: multipart/form-data
File: CSV file with a text column.

### Response
Summary of sentiments.
Detailed results including sentiment scores and categories.

### Example Response

{
  "summary": {
    "total_entries": 3,
    "positive_count": 1,
    "negative_count": 2,
    "neutral_count": 0
  },
  "details": [
    {
      "id": 1,
      "text": "I love the new features of this product!",
      "sentiment": "positive",
      "sentiment_score": 0.6696
    },
    {
      "id": 2,
      "text": "The service was okay, nothing special.",
      "sentiment": "negative",
      "sentiment_score": -0.092
    },
    {
      "id": 3,
      "text": "I am not happy with the recent changes.",
      "sentiment": "negative",
      "sentiment_score": -0.4585
    }
  ]
}

## Deployment
The backend is deployed on Render.

## Deployment Steps

1. Prepare your repository: Ensure requirements.txt and app/main.py are present in the root folder.
2. Deploy to Render:

- Log in to Render and create a new web service.
- Connect your GitHub repository.
- Set the build command: pip install -r requirements.txt
- Set the start command: uvicorn app.main:app --host 0.0.0.0 --port 8000

### Contributing
Contributions are welcome! To contribute:

1.Fork the repository.
2. Create a feature branch (git checkout -b feature-name).
3. Commit your changes (git commit -m "Add new feature").
4. Push to the branch (git push origin feature-name).
5. Create a pull request.

### License
This project is licensed under the MIT License.

