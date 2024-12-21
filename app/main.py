from fastapi import FastAPI, File, UploadFile
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from fastapi.responses import JSONResponse

app = FastAPI()

# Initialize Sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()

@app.post("/analyze")
async def analyze_csv(file: UploadFile = File(...)):
    try:
        # Read the uploaded CSV file
        df = pd.read_csv(file.file)
        if "text" not in df.columns:
            return JSONResponse(
                status_code=400, 
                content={"error": "CSV must include a 'text' column"}
            )
        
        # Perform sentiment analysis
        df['sentiment'] = df['text'].apply(lambda x: analyze_sentiment(x))
        df['sentiment_score'] = df['text'].apply(lambda x: analyzer.polarity_scores(x)['compound'])

        # Return results as JSON
        return df.to_dict(orient='records')
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

def analyze_sentiment(text):
    """Perform sentiment analysis using VADER"""
    scores = analyzer.polarity_scores(text)
    if scores['compound'] > 0.05:
        return 'positive'
    elif scores['compound'] < -0.05:
        return 'negative'
    else:
        return 'neutral'

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
