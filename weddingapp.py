from bottle import request, route, template, run, jinja2_view, redirect, static_file
import functools
import os

view = functools.partial(jinja2_view, template_lookup=['templates'])
subps = ['start.html', 'agenda.html', 'drive.html', 'hotels.html', 'music.html', 'picture.html', 'checkin.html']
    
# handler for static files
@route('/static/:path#.+#', name='static')
def static(path):
    subp = 'content_' + path
    if path == subps[5]:
        return template('templates/template.html', subp=subp, res=picres())
    elif path in subps:
        subp = 'content_' + path
        if os.path.isfile('templates/' + subp):
            return template('templates/template.html', subp=subp)
        else:
            return template('templates/template.html', subp='')
    return static_file(path, root='static')
    
@route('/pictures/:path#.+#', name='pictures')
def static(path):
    return static_file(path, root='pictures')
    
# Test
@route('/app/<name>/<surname>')
def hello_name(name, surname):
    return "Hello " + name + ", " + surname

# website routing
@route("/")
#@view('template.html')
def startup():
#    return dict(subp='agenda')
#    return static_file("start.html", root="static/")
    return template('templates/template.html', subp='content_start.html')

def picres():
    res = [f for f in os.listdir('pictures') if os.path.isfile(os.path.join('pictures', f))] # take all filenames from directory
    res = [k for k in res if 'jpg' in k.lower()] # put in list if contains jpg
    res.sort()
    nms = [w.replace(".jpg", "") for w in res] # remove the .jpg
    nms = [w.replace(".JPG", "") for w in nms] # remove the .jpg
    res = [res, nms] # put in one list
    return map(list, zip(*res)) # transpose

# server run
if __name__ == "__main__":
#    run(server="flup", host='localhost', port=8080)
    run(host='0.0.0.0', port=8080)


#from werkzeug.contrib.fixers import LighttpdCGIRootFix
#app = Flask(__name__)
#app.wsgi_app = LighttpdCGIRootFix(app.wsgi_app)
#    app.run(host="localhost", port=8080)
#    app.run(port=8080,host='0.0.0.0',ssl_context='adhoc')
