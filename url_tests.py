from main import app
from fastapi.testclient import TestClient
from model import URLModel

client = TestClient(app)

def test_database_connection():
    test_short_url = "test1234"
    test_long_url = "https://www.test.com"
    URLModel(short_url=test_short_url, long_url=test_long_url).save()

    retrieved_url = URLModel.get(test_short_url)
    assert retrieved_url.short_url == test_long_url

    retrieved_url.delete()

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "This is the url-shortener app."}

def test_shorten_url():
    sample_payload = {
        "long_url": "www.test_url.com",
        "short_url": "test_short_url"
    }
    response = client.post("/shorten_url", json=sample_payload)
    assert response.status_code == 201
    assert response.json() == {
        "Success": "url to be shortened: url=www.test_url.com, short_url=test_short_url"
    }

def test_get_url():
    response = client.get("/redirect/test_short_url")
    assert response.status_code == 200
    assert response.json() == {
        "www.test_url.com"
    }

def test_delete_url():
    response = client.delete("/delete/test_short_url")
    assert response.status_code == 200
    assert response.json() == {
       "Success": "Deleted url with short url: test_short_url"
    }

def test_short_not_found():
    response = client.get("/redirect/test_short_url")
    assert response.status_code == 400
    assert response.json() == {
        "detail": "No URL for short url: `test_short_url` found."
    }