from app.models.model import URLModel
from pynamodb.connection import Connection
from pynamodb.exceptions import DoesNotExist
from pynamodb.exceptions import DeleteError

table = URLModel.Meta.table_name
# to run locally: 
# connection = Connection(host='http://localhost:8000')
# to run on AWS:
connection = Connection()

class Database(URLModel):
    def list_urls():
        urls = {}
        for item in URLModel.scan():
            urls[item.short_url] = item.long_url
        return urls

    def get(short_url: str):
        response = connection.get_item(table_name=table, hash_key=short_url)
        return response["Item"]['long_url']

    def create(short_url: str, long_url: str):
        URLModel(short_url=short_url, long_url=long_url).save()
 

    def exists(short_url):
        try:
            response = connection.get_item(table_name=table, hash_key=short_url)
            return 'Item' in response
        except DoesNotExist:
            return False
    
    def delete(short_url):
            # connection.delete_item(table_name=table, hash_key=short_url)
            try:
                connection.delete_item(table_name=table, hash_key=short_url)
            except DeleteError as e:
                print(f"Failed to delete item: {e}")