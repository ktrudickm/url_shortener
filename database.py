from model import URLModel
from pynamodb.connection import Connection
from pynamodb.exceptions import DoesNotExist

table = URLModel.Meta.table_name
connection = Connection(host='http://localhost:8000')

class Database(URLModel):
    def list_urls():
        return URLModel.scan()

    def get(short_url: str):
        response = connection.get_item(table_name=table, hash_key=short_url)
        return response["Item"]['long_url']

    def create(short_url: str, long_url: str):
        URLModel(short_url=short_url, long_url=long_url).save()
    

    def exists(short_url):
        response = connection.get_item(table_name=table, hash_key=short_url)
        if not 'Item' in response:
            return False
        else:
            return True
 

