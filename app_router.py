from fastapi import APIRouter, HTTPException
from fetch import fetch_jokes_from_api
from db import save_jokes_to_db

router = APIRouter()

@router.post("/fetch-jokes")
def fetch_jokes():
    try:
        all_jokes = []
        total_jokes_needed = 100  
        jokes_per_request = 10 
        total_jokes_fetched = 0
        
     
        while total_jokes_fetched < total_jokes_needed:
            jokes_data = fetch_jokes_from_api(amount=jokes_per_request)
            jokes = jokes_data.get("jokes", [])
            
            if not jokes:
                raise HTTPException(status_code=400, detail="No jokes found in API response")
            
            all_jokes.extend(jokes)
            total_jokes_fetched += len(jokes)

        # Save jokes to the database
        save_jokes_to_db(all_jokes)
        return {"message": f"Successfully fetched and saved {len(all_jokes)} jokes."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
