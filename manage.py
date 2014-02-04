from flask.ext.assets import ManageAssets
from flask.ext.script import Manager, Shell, Server
from flask.ext.security.script import CreateUserCommand

from app import app

manager = Manager(app)
#manager.add_command("assets", ManageAssets())
manager.add_command('create_user', CreateUserCommand())
manager.add_command("runserver", Server(host="10.0.2.15",
                                                 port=5000))
manager.add_command("shell", Shell())

if __name__ == "__main__":
    manager.run()