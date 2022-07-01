from fastapi import FastAPI, HTTPException, Path
from starlette.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import re

app = FastAPI()

@app.get("/")
def index():
    return RedirectResponse(url="/docs/")

@app.get("/v1/api/patent/id/{patent_id}")
async def get_by_id(patent_id: int = PATH(title="The ID of the item to get")):
    #if patent_id.isdigit():
    return {"id": patent_id}
    #else:
    #    return {"error": "The id patent must be an integer"}

@app.get("/v1/api/patent/number/{patent_number}")
async def get_by_patent(patent_number: str = PATH(title="The PATENT of the item to get")):
    regex = re.compile("[A-Z]{4}[0-9]{3}$")
    if regex.match(patent_number):
        return {"patent": patent_number}
    else:
        raise HTTPException(status_code=402, detail={"error": "The patent number must be type as: AAAA000 or ZZXD758"})
