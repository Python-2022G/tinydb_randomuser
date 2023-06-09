from tinydb import TinyDB
from api import get_users

db = TinyDB('data.json', indent=4)

# users = get_users(30, 'female')

male_users_table = db.table('male_users')
# male_users_table.insert_multiple(users)

print(male_users_table.all())