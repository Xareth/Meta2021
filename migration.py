from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from server.config import app, db
from models import m_users, m_privileges, m_logs


migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()


# heroku run python (its NOT necessary during migration)
# flask db stamp head
# python migration.py db migrate
# python migration.py db upgrade
