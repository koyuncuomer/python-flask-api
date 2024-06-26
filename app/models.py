from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(120), unique=True)
    address = db.Column(db.JSON)
    phone = db.Column(db.String(20))
    website = db.Column(db.String(100))
    company = db.Column(db.JSON)

    posts = db.relationship('Post', backref='user', lazy=True)
    todos = db.relationship('Todo', backref='user', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'username': self.username,
            'email': self.email,
            'address': self.address,
            'phone': self.phone,
            'website': self.website,
            'company': self.company
        }


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(200))
    body = db.Column(db.Text)

    comments = db.relationship('Comment', backref='post', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'userId': self.user_id,
            'title': self.title,
            'body': self.body
        }


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120))
    body = db.Column(db.Text)

    def to_dict(self):
        return {
            'id': self.id,
            'postId': self.post_id,
            'name': self.name,
            'email': self.email,
            'body': self.body
        }


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(200))
    completed = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            'id': self.id,
            'userId': self.user_id,
            'title': self.title,
            'completed': self.completed
        }
