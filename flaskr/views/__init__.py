from flask import render_template
from datetime import date
from dateutil.relativedelta import relativedelta
from flaskr import app
from flaskr.models import Person

@app.route('/')
def index():
    today = date.today()
    prev = date.today() - relativedelta(months=1)
    yymm = today.strftime('%Y%m')
    items = []
    persons = Person.query.filter(Person.enabled==True).order_by(Person.staff.asc(), Person.name.asc()).all()
    for person in persons:
        item = {}
        item['id'] = person.id
        item['name'] = person.get_display()
        item['staff'] = person.staff
        item['yymm'] = yymm
        item['yymm1'] = prev.strftime('%Y%m')
        items.append(item)
    return render_template('index.pug', items=items)

from flaskr.views import persons
app.register_blueprint(persons.bp)
from flaskr.views import performlogs
app.register_blueprint(performlogs.bp)
from flaskr.views import worklogs
app.register_blueprint(worklogs.bp)
from flaskr.views import timerules
app.register_blueprint(timerules.bp)
from flaskr.views import options
app.register_blueprint(options.bp)
from flaskr.views import users
app.register_blueprint(users.bp)
from flaskr.views import auth
app.register_blueprint(auth.bp)
