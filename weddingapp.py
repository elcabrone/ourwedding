from bottle import request, route, template, run, jinja2_view, redirect
import sqlite3
import functools

view = functools.partial(jinja2_view, template_lookup=['templates'])

# db management
conn = sqlite3.connect('wedding.db', check_same_thread=False)
c = conn.cursor()

@route('/app/<name>')
def hello_name(name):
    return "Hello " + name

# website routing
@route("/")
@view('wedding.html')
def startup():
    cur = conn.execute('SELECT * from milestones')
    milestones = cur.fetchall()
    return dict(milestones=milestones, admin=0)

@route("/admin")
@view('wedding.html')
def admin():
    cur = conn.execute('SELECT * from milestones')
    milestones = cur.fetchall()
    return dict(milestones=milestones, admin=1)

@route("/add", method='POST')
def add():
    c.execute("insert into milestones (activity, schedule, location) values (?, ?, ?)",
        [request.forms['activity'], request.forms['schedule'], request.forms['location']]) 
    conn.commit()
    return redirect('/')

@route("/del/<number>")
def delete(number):
    c.execute("delete from milestones where MID=?", number)
    conn.commit()
    return redirect('/')    
    
@route("/init")
def init():
    with open('wedding_schema.sql', 'r') as f:
        c.executescript(f.read())
    return redirect('/')

# server run
if __name__ == "__main__":
#    run(server="flup", host='localhost', port=8080)
    run(host='localhost', port=8080)


#from werkzeug.contrib.fixers import LighttpdCGIRootFix
#app = Flask(__name__)
#app.wsgi_app = LighttpdCGIRootFix(app.wsgi_app)
#    app.run(host="localhost", port=8080)
#    app.run(port=8080,host='0.0.0.0',ssl_context='adhoc')
