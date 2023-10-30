from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute

class Table(Model):
    class Meta:
        region = 'us-east-1'
        host = 'http://localhost:8000'

# definition of data model/structure of data
# layer of abstraction between the database and the application
class URLModel(Table):
    class Meta:
        table_name = 'url-table'
        read_capacity_units = 1
        write_capacity_units = 1
    short_url = UnicodeAttribute(hash_key=True)
    long_url = UnicodeAttribute()
