#!/usr/bin/env python
from flask.ext.script import Manager, Shell, Server
from flask_assets import ManageAssets
from control import app,assets_env

manager = Manager(app)
manager.add_command("assets", ManageAssets(assets_env))
manager.add_command("runserver", Server(host="10.0.2.15", port=8000))
manager.add_command("shell", Shell())
manager.run()