from src.model.user import User
from src.model.base import db

admin = User(title='admin', release_date='dssd')
guest = User(title='guest', release_date='ds')

db.session.add(admin)
db.session.add(guest)
db.session.commit()

print(User.query.all())
