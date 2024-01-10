from peewee import *

db = MySQLDatabase('tienda_online', user='root', password='', host='localhost', port=3306)


class BaseModel(Model):
   class Meta:
    database = db