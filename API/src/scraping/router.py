from fastapi import APIRouter, HTTPException
from annenbergscraper import scrape_articles


router = APIRouter()

@router.get("/scrape/")
async def scrape_endpoint(url: str):
    try:
        data = scrape_articles()
        return {"status": "success", "data": data}
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))