from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute

# definition of data model/structure of data
# layer of abstraction between the database and the application
class URLModel(Model):
    class Meta:
        region = 'us-east-2'
        # host = 'http://localhost:8000'
        table_name = 'url-table'
    short_url = UnicodeAttribute(hash_key=True)
    long_url = UnicodeAttribute()
