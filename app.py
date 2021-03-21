from server.config import app, db
from apps.users import sv_users, sv_login
from apps.general import sv_general
from apps.logs import sv_logs
from flask_migrate import Migrate

migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
