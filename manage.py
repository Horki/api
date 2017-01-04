from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from api.app import app, db
from api.commands.TestsCommand import TestsCommand
from api.commands.SeedCommand import SeedCommand
from api.app.models.User import User
from api.app.models.Book import Book


migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)
manager.add_command('seed', SeedCommand)
manager.add_command('test', TestsCommand)

if __name__ == '__main__':
    manager.run()
