from server.config import db


role_user = db.Table("role_user", db.metadata,
                     db.Column('role_id', db.Integer, db.ForeignKey('roles.id')),
                     db.Column('user_id', db.Integer, db.ForeignKey('users.id'))
)


privilege_role = db.Table("privilege_role", db.metadata,
                          db.Column('privilege_id', db.Integer, db.ForeignKey('privileges.id')),
                          db.Column('role_id', db.Integer, db.ForeignKey('roles.id'))
)


class Privilege(db.Model):
    __tablename__ = "privileges"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String)
    description = db.Column(db.String)
    role_id = db.relationship("Role",
                            secondary=privilege_role, backref="privileges", lazy="dynamic")

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Uprawnienie {self.name}'


class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String)
    privilege_id = db.relationship("Privilege",
                              secondary=privilege_role, backref="roles", lazy="dynamic")
    user_id = db.relationship("User",
                                   secondary=role_user, backref="roles", lazy="dynamic")

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Uprawnienie {self.name}'

