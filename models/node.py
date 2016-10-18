from . import ModelMixin
from . import db
from . import timestamp


class Node(db.Model, ModelMixin):
    __tablename__ = 'nodes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    title = db.Column(db.String())
    avatar = db.Column(db.String())
    topics = db.relationship('Topic', backref='node')

    def __init__(self, form):
        self.name = form.get('name', '')
        self.avatar = form.get('avatar', '')
        self.title = form.get('title', '')

    def update(self, form):
        self.name = form.get('name', '')
        self.avatar = form.get('avatar', '')
        self.title = form.get('title', '')
        self.save()