from model import URLModel
from pynamodb.connection import TableConnection


# if not URLModel.exists():
#     URLModel.create_table(read_capacity_units=1, write_capacity_units=1)

class Database:
    def __init__(self):
        self.table = URLModel
        self.connection = TableConnection(self.table.Meta.table_name)

    def create(self, short_url, long_url):
        self.table(short_url, long_url).save()

    def get(self, short_url):
        return self.table.get(short_url)

    def list(self):
        return self.connection.scan()

    def exists(self, short_url):
        return self.table.exists(short_url)



