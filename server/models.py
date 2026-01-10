from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# ------------------------
# User Model
# ------------------------
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    # Add any other fields you need (like password, email, etc.)

    articles = db.relationship('Article', backref='author', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username
        }

# ------------------------
# Article Model
# ------------------------
class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'user_id': self.user_id
        }
