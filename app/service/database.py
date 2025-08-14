from app.models.model import URLModel
from pynamodb.exceptions import DoesNotExist

class Database:
    @staticmethod
    def list_urls():
        urls = {}
        for item in URLModel.scan():
            urls[item.short_url] = item.long_url
        return urls

    @staticmethod
    def get(short_url: str):
        try:
            url_model = URLModel.get(short_url)
            return url_model.long_url
        except DoesNotExist:
            return None

    @staticmethod
    def create(short_url: str, long_url: str):
        URLModel(short_url=short_url, long_url=long_url).save()

    @staticmethod
    def exists(short_url):
        try:
            URLModel.get(short_url)
            return True
        except DoesNotExist:
            return False

    @staticmethod
    def delete(short_url):
        try:
            url_model = URLModel.get(short_url)
            url_model.delete()
        except DoesNotExist as e:
            print(f"Failed to delete item: {e}")