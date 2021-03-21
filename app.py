from server.config import app, db
from server import sv_general, sv_login, sv_users, sv_logs
from models import m_users, m_logs
from flask_migrate import Migrate, MigrateCommand

migrate = Migrate(app, db)



if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )


