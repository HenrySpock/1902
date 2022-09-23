from flask import Flask, request, render_template
from random import randint, choice, sample
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "so-secret"  #this has to do with sessions, and was introduced in the 
#debug toolbar section - this file currently loads properly, so it should be correct
debug = DebugToolbarExtension(app)  

@app.route('/')
def welc():
    return "Well howdy!"
    #the '/' endpoint is considered the 'root'

# hello v1
# @app.route('/hello')  
# def hello(): 
#     return "HELLO THERE!"
    #this successfully returns the text in an unformatted state - not HTML, just a python string
    
# hello v2
@app.route('/hello')  
def hello(): 
    html = "<html><body><h1>Hello</h1></body></html>"
    return html    
    #In the video, the demonstration shows the app.route serving this HTML formatted to the screen 
    #like you would expect from an HTML file. Here it's simply shown on one line. This is not the 
    #typical way things are done - usually render_template is used.

#goodbye v1
# @app.route('/goodbye')
# def say_bye():
#     return "GOOD BYE!!!"

#goodbye v2
@app.route('/goodbye')
def say_bye():
    html = "<html><body><h1>Adios!</h1></body></html>"
    return html

@app.route('/eval')  
def temp(): 
    msg = "This is the temp_test endpoint."
    return render_template("index.html", msg = msg)
    #this successfully renders the index.html file

@app.route('/lucky')
def luck():
    num = randint(1, 5)
    return render_template('lucky.html', lnum = num)

#19 02 05 GREETER DEMO
COMPLIMENTS = ["cool", "clever", "tenacious", "awesome", "Pythonic", "Cybertronic", "rad", "tubular", "sharp", "clever girl" ]

@app.route('/form')
def show_form():
    return render_template("form.html")

@app.route('/greet')
def get_greeting():
    usergreet = request.args["username"]
    compliment = choice(COMPLIMENTS)
    return render_template("greet.html", usergreet=usergreet, comp = compliment) 
#username in request.args is defined on the form.html "name=""
#in the return statement, usergreet on left is  variable to be passed to the 
#next route, usergreet on the right is the variable passed from request.args

@app.route('/form2')
def show_form_2():
    return render_template("form2.html")

@app.route('/greet2')    
def shgr2():
    username = request.args["username"]
    #wcom = request.args["wcom"]
    wcom = request.args.get("wcom")
    nicety = sample(COMPLIMENTS, 3)
    return render_template("greet2.html", usergreet=username, wcom=wcom, nicety=nicety)
    #Notice: wcom above refers to an on/off variable from a checkbox: if it's check, the query
    #string successfully returns wcom=on, but if it's not checked, you get a bad request key
    #error,so instead of simply using request.args["wcom"], we use request.args.get["wcom"]. 
    #Remember, .get is a method, so it's .get() instead of .args[]. All this does is prevent 
    #the thrown error from wcom not being defined.

@app.route('/spell/<word>')
def spell_word(word):
    capw = word.upper()
    return render_template('sp_w.html', word=capw)

@app.route('/base')
def base(): 
    return render_template("base.html")