from fastapi import FastAPI
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from textSummarizer.pipeline.prediction_pipeline import PredictionPipeline


text:str = "what is Text Summarization?"

app = FastAPI()

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse("/docs")



@app.get("/train")
async def train():
    try:
        os.system("python main.py")
        return Response("Training successful !")
    except Exception as e:
        return Response(f"Error occurred: {str(e)}")
    


@app.get("/predict")
async def predict(text):
    try:
        obj = PredictionPipeline()
        text = obj.predict(text)
        return text
    except Exception as e:
        raise e
    

if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)