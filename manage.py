#!/usr/bin/env python
from flask.ext.script import Manager, Shell, Server
from control import app

manager = Manager(app)
manager.add_command("runserver", Server(host="10.0.2.15", port=5000))
manager.add_command("shell", Shell())
manager.run()