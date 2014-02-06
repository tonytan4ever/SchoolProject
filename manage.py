from flask.ext.assets import ManageAssets
from flask.ext.script import Manager, Shell, Server
from flask.ext.script.commands import  ShowUrls
#from flask.ext.security.script import CreateUserCommand, \
#                                            DeleteUserCommand, ListUsersCommand

from framework.app import create_app 
from framework.factory import db

manager = Manager(create_app())


@manager.command
def initdb():
    """Init/reset database."""

    db.drop_all()
    db.create_all()

    #===========================================================================
    # admin = User(
    #        username=u'admin',
    #        email=u'admin@example.com',
    #        password=encrypt_password('password'),
    #        #role_code=ADMIN,
    #        active=True,
    #        #status_code=ACTIVE,
    #        user_detail=UserDetail(
    #            sex_code=MALE,
    #            age=10,
    #            url=u'http://admin.example.com',
    #            deposit=100.00,
    #            location=u'Hangzhou',
    #            bio=u'admin Guy is ... hmm ... just a admin guy.'))
    # 
    # db.session.add(admin)
    # db.session.commit()
    #===========================================================================
    
    #===========================================================================
    # for role_key in ROLES:
    #    r = Role(name=role_key, description=ROLES[role_key])
    #    db.session.add(r)
    #    admin.roles.append(r)
    #    db.session.commit()
    #    
    # db.session.add(admin)
    # db.session.commit()
    #===========================================================================
    
    
#manager.add_command("assets", ManageAssets())
#manager.add_command('create_user', CreateUserCommand())
#manager.add_command('delete_user', DeleteUserCommand())
#manager.add_command('list_users', ListUsersCommand())

manager.add_command("runserver", Server(host="10.0.2.15",
                                                 port=5000))
manager.add_command("shell", Shell())
manager.add_command("list_url", ShowUrls())

if __name__ == "__main__":
    manager.run()