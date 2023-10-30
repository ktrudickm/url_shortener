from uuid import uuid4

# Generate a short url from a long url using uuid4
def generate_short_url(long_url: str):
    uuid = uuid4()
    short_url = str(uuid)[:7]
    return short_url

