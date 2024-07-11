from datetime import datetime
from app import db

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(256))
    pub_date = db.Column(db.DateTime, default=datetime.today)

    def __repr__(self):
        return f'<News {self.title}>'

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    news_id = db.Column(db.Integer, db.ForeignKey('news.id'), nullable=False)
    body = db.Column(db.Text, nullable=False)
    pub_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Comment {self.body[:20]}>'
