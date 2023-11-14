from fastapi import APIRouter, status, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from typing import Optional
import validators
from utils.uuid_generator import generate_short_url
from database import Database

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
    return Database.list_urls()

# GET /redirect(short_url) → This endpoint takes a short_url as a parameter and returns the original URL.
@router.get('/redirect/{short_url}')
def get_original_url(short_url: str):
    # if short_url does not exist in database, return 404:
    if Database.exists(short_url):
        return RedirectResponse(Database.get(short_url)['S'], status_code = 200)
        
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"No URL for short url: `{short_url}` found.")

# POST /shorten_url(url, short_url: optional) : This endpoint creates a shortened version of a given URL. 
# Optionally, users can also provide a custom short_url
@router.post('/shorten_url')
def shorten_url(url: URL):
    # Check if the short url is already in the database
    if url.short_url and Database.exists(url.short_url):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Short URL {url.short_url} already exists. Try a different short url.")   

    # Check if the url is a valid url
    if not validators.url(url.long_url):
        return {"Error": "Invalid URL"}
    
    # Generate a short url if not provided - making sure it is unique
    if not url.short_url:
        short = generate_short_url(url.long_url)
        while Database.exists(short):
            short = generate_short_url(url.long_url)
        url.short_url = short


    # Add the urls to the database
    Database.create(url.short_url, url.long_url)
    return {"Success": f"url to be shortened: url={url.long_url}, short_url={url.short_url}"}

# Delete route used for testing purposes
@router.delete('/delete/{short_url}')
def delete_url(short_url: str):
    if Database.exists(short_url):
        Database.delete(short_url)
        return {"Success": f"Deleted url with short url: {short_url}"}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"No URL for short url: `{short_url}` found.")