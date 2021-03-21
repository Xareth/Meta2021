from server.config import db


def add(func):
    def wrapper(*args, **kwargs):
        db.session.add(func(*args, **kwargs))
        db.session.commit()
    return wrapper


def update(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        db.session.commit()
    return wrapper
