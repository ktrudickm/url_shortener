from fastapi import APIRouter, Response, status, HTTPException
from pydantic import BaseModel
from typing import Optional
import validators
from uuid_generator import generate_short_url

router = APIRouter()

# Temporary database for testing routes
temp_db = {'test123': 'https://www.google.com', 'ae184bc7': 'https://www.youtube.com'}

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
    return {"message": f"These are all the shortened urls. {temp_db}"}

# GET /redirect(short_url) → This endpoint takes a short_url as a parameter and returns the original URL.
@router.get('/redirect/{short_url}')
def get_original_url(short_url: str):
    # if short url does not exist in database, return 404:
    if short_url not in temp_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No URL found for {short_url} found.")
    return {"message": f"This is the original url: {temp_db[short_url]}."}

# POST /shorten_url(url, short_url: optional) : This endpoint creates a shortened version of a given URL. 
# Optionally, users can also provide a custom short_url
# Return 404 error if user gives a short url that is already being used
@router.post('/shorten_url')
def shorten_url(url: URL):
    # Check if the short url is already in the database
    if url.short_url in temp_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Short URL {url.short_url} already exists.")   

    # Check if the url is a valid url
    if not validators.url(url.long_url):
        return {"Error": "Invalid URL"}
    
    # Generate a short url if not provided
    if not url.short_url:
        url.short_url = generate_short_url(url.long_url)

    # Add the urls to the database
    temp_db[url.short_url] = url.long_url
    return {"Success": f"url to be shortened: url={url.long_url}, short_url={url.short_url}"}