from tinydb import TinyDB
from api import get_users

db = TinyDB('data.json', indent=4)

users = get_users(30)
db.insert_multiple(users)