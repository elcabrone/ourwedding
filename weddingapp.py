
from bottle import request, route, template, run, jinja2_view, redirect, static_file, default_app, SimpleTemplate, request
import functools
import os

view = functools.partial(jinja2_view, template_lookup=['templates'])
subps = ['start.html', 'agenda.html', 'drive.html', 'hotels.html', 'music.html', 'picture.html', 'checkin.html']
piccap = ['01. Wolfenbu\xcc\x88ttel 2007', '02. Silvester 2007 2008', '03. TG Ball 2008', '04. Dresden 2009', '05. Disneyland Paris 2010 2011', '06. Lissabon 2012', '07. Hochzeit Caro und Nils 2013', '08. Sydney 2013', '09. Western Australia 2013', '10. Verona 2014', '11. Bulgarien 2015', '12. Rom 2016', '13. Ingolstadt 2016', '14. Standesamt 2016', '15. Babybauch 2017', '16. Babybauch 2017 2', '17. Sarah 13.03.2017', '18. Sarah 17.03.17', '19. Sarah 18.03.17', '20. Sarah 21.03.2017', '21. Erstes Familienfoto 2017', '22. Zweites Familienfoto 2017']
    
# handler for static files
@route('/static/:path#.+#')
def static(path):
    subp = 'content_' + path
    if path == subps[5]:
        return template('templates/template.html', subp=subp, res=piccap)
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
    
@route('/register', method='POST')
def register():
    postdata = request.body.read()
    print(postdata)
    name=str(request.forms.get('person'))
    resp=str(request.forms.get('response'))
    pers=str(request.forms.get('anzahl'))
    vegi=str(request.forms.get('vegetarisch'))

    with open("responses", 'a') as f:
        f.write('Name: ' + name + ', Antwort: ' + resp + ', Personenzahl: ' + pers + ', Vegetarier: ' + vegi + '\n')
    return redirect('http://ourwedding.cloud/krost')

# Test
@route('/test/:vari')
def test(vari='Test'):
	return "Test: " + os.getcwd() + " - " + vari

# website routing
@route("/")
@route("/krost")
def loader():
	return redirect("http://ourwedding.cloud/krost/start")

@route("/start")
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
    run(server="flup", host='0.0.0.0', port=8080)
#    run(host='0.0.0.0', port=8080)


#from werkzeug.contrib.fixers import LighttpdCGIRootFix
#app = Flask(__name__)
#app.wsgi_app = LighttpdCGIRootFix(app.wsgi_app)
#app.run(host="localhost", port=8080)
#app.run(port=8080,host='0.0.0.0',ssl_context='adhoc')
