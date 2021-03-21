from server.config import ma
from models.m_users import User
from models.m_logs import Log
from models.m_privileges import Privilege


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
