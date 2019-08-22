# Python Flask Project

After using blueprints:

To do database changes in the Terminal:

from app import create_app, db

app = create_app()

ctx = app.app_context()

ctx.push()

db.create_all()

ctx.pop()

exit()