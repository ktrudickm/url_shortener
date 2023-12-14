from app.main import app
from fastapi.testclient import TestClient
from app.models.model import URLModel
from fastapi.responses import RedirectResponse

#  pytest url_tests.py -vv -s

client = TestClient(app)

def test_database_connection():
    test_short_url = "test1234"
    test_long_url = "https://www.test.com"
    URLModel(short_url=test_short_url, long_url=test_long_url).save()

    retrieved_url = URLModel.get(test_short_url)
    assert retrieved_url.long_url == test_long_url

    retrieved_url.delete()

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "This is the url-shortener app."}

# Test successful creation of short url
def test_shorten_url():
    sample_payload = {
        "long_url": "https://www.testurl.com",
        "short_url": "test_short_url"
    }
    response = client.post("/shorten_url", json=sample_payload)
    assert response.status_code == 200
    assert response.json() == {
        "short_url": ["test_short_url"], "original_url": ["https://www.testurl.com"]
    }

# Test invalid url attempting to be shortened
def test_invalid_url():
    sample_payload = {
        "long_url": "htps:/testurl",
        "short_url": "test_url"
    }
    response = client.post("/shorten_url", json=sample_payload)
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Error: Invalid URL."
    }


# Test attempting to shorten a url that already exists
def test_duplicate_short_url():
    sample_payload = {
        "long_url": "https://www.testurl.com",
        "short_url": "test_short_url"
    }
    response = client.post("/shorten_url", json=sample_payload)
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Short URL test_short_url already exists. Try a different short url."
    }

# Test successfully retrieving the original url from a short url
def test_get_url():
    response = client.get("/redirect/test_short_url", allow_redirects=False)
    assert response.status_code == 302
    assert response.headers['Location'] == "https://www.testurl.com"
    
# Test retrieving a short url that does not exist
def test_short_not_found():
    response = client.get("/redirect/test_short")
    assert response.status_code == 400
    assert response.json() == {
        "detail": "No URL for short url: `test_short` found."
    }

# Test successfully deleting a short url
def test_delete_url():
    response = client.delete("/delete/test_short_url")
    assert response.status_code == 200
    assert response.json() == {
       "short_url": ["test_short_url"]
    }

# Test deleting a short url that does not exist
def test_delete_url_not_found():
    response = client.delete("/delete/test_short")
    assert response.status_code == 400
    assert response.json() == {
        "detail": "No URL for short url: `test_short` found."
    }