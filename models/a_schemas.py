from server.config import ma
from models.m_users import User
from models.m_logs import Log


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
