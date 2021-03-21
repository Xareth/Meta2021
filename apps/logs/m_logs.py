from server.config import db


class Log(db.Model):
    __tablename__ = "logs"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    category = db.Column(db.String)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    message = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f"({self.category}): {self.message}"

