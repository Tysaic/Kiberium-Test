from fastapi import FastAPI, HTTPException, Path, Depends
from starlette.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from dbengine.database import SessionLocal, engine
from models.models import Base
from functions import patent_by_id, patent_by_number
import re

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def index():
    return RedirectResponse(url="/docs/")

@app.get("/v1/api/patent/id/{patent_id}")
async def get_by_id(
        patent_id: int = Path(title="The ID of the item to get", gt=0), 
        db: Session = Depends(get_db)
    ):
    get_pattern_number = patent_by_id(db, patent_id)
    if get_pattern_number:
        return {"patent": get_pattern_number.number}
    else:
        raise HTTPException(status_code=422, detail={"alert": "ID doesn't exists"})

@app.get("/v1/api/patent/number/{patent_number}")
async def get_by_number(
        patent_number: str = Path(title="The PATENT of the item to get"),
        db: Session = Depends(get_db)
    ):
    regex = re.compile("[A-Z]{4}[0-9]{3}$")
    if regex.match(patent_number):
        get_pattern_id = patent_by_number(db, patent_number)
        if get_pattern_id:
            return {"id": get_pattern_id.id}
        else:
            raise HTTPException(status_code=422, detail={"alert": "The patent doesn't exists"})
    else:
        raise HTTPException(status_code=422, detail={"error": "The patent number must be type as: AAAA000 4 letters and 3 digits"})
