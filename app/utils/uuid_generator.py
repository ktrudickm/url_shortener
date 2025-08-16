from uuid import uuid4

def encode_base62(num: int):
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    base = len(chars)
    encoded = ""
    while num > 0:
        num, rem = divmod(num, base)
        encoded = chars[rem] + encoded
    return encoded or chars[0]

# Generate a short url from a long url using uuid4
def generate_short_url(long_url: str):
    uuid = uuid4()
    u_int = uuid.int
    short_url = encode_base62(u_int)[:6]
    return short_url

