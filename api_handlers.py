from fastapi import APIRouter, Response, status, HTTPException
from pydantic import BaseModel
from typing import Optional
import validators

router = APIRouter()

# Define a URL model with long and short URL attributes
class URL(BaseModel):
    long_url: str
    short_url: Optional[str] = None

# GET / → This endpoint returns a simple message to make sure that the server is up and running.
@router.get('/')
def read_root():
    return {"message": "This is the url-shortener app."}

# GET /list_urls → This endpoint returns a list of all the shortened URLs.
@router.get('/list_urls')
def list_urls():
    return {"message": "These are all the shortened urls."}

# GET /redirect(short_url) → This endpoint takes a short_url as a parameter and returns the original URL.
@router.get('/redirect/{short_url}')
def get_original_url(short_url: str, response = Response):
    # if short url does not exist in database, return 404:
    # if short url not in database:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No URL found for {short_url} found.")
    return {"message": "This is the original url."}

# POST /shorten_url(url, short_url: optional) : This endpoint creates a shortened version of a given URL. 
# Optionally, users can also provide a custom short_url
# Return 404 error if user gives a short url that is already being used
@router.post('/shorten_url')
def shorten_url(url: URL, response = Response):
    print(url.dict())
    # Check if the short url is already in the database
    # if short url in database:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Short URL {url.short_url} already exists.")   

    # Check if the url is a valid url
    if not validators.url(url.long_url):
        return {"Error": "Invalid URL"}
    return {"Success": f"url to be shortened: url={url.long_url}, short_url={url.short_url}"}