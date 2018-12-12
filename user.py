from src.model.base import db


class User(db.Model):
    __tablename__ = 'test'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column('TITLE', db.String(80), unique=False, nullable=False)
    release_date = db.Column(db.String(80), unique=False, nullable=False)

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

    def __repr__(self):
        return '<User %r>' % self.title


db.create_all()
