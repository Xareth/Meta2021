from server.config import ma
from apps.users.m_users import User


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
