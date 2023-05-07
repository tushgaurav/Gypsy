from fastapi import FastAPI
from pydantic import BaseModel


class Search(BaseModel): 
    Text: str
    MaxResults: int


app = FastAPI()
    

@app.get("/api/search/")
async def search(text: str, maxResults: int = 5):
    return {
        "text": text,
        "maxResults": maxResults
    }
