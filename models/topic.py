from . import ModelMixin
from . import db
from . import timestamp


class Topic(db.Model, ModelMixin):
    __tablename__ = 'topics'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    content = db.Column(db.String())
    created_time = db.Column(db.Integer, default=0)
    node_id = db.Column(db.Integer, db.ForeignKey('nodes.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comment', backref='topic')



    def __init__(self, form):
        self.title = form.get('title', '')
        self.content = form.get('content', '')
        self.created_time = timestamp()




    def update(self, form):
        self.title = form.get('title', '')
        self.content = form.get('content', '')
        self.save()
