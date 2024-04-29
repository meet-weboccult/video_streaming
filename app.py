from flask import Flask, render_template, redirect, url_for, request, session,Response
from flask_session import Session
from redis import Redis
from authentication import Authentication
import socketio

Flask.jinja_options = { 'line_statement_prefix': '#'}
app = Flask(__name__)
authenticator = Authentication()

@app.get('/')
def login():
    if authenticator.is_loggedin:
        return redirect(url_for("home"))
    
    return render_template('login.html')

@app.post('/')
def authenticate():
    login_success = authenticator.login(request.form)
    if login_success:
        return redirect(url_for("home"))

    return render_template('login.html', login_success = False)

@app.get("/home")
def home():
    if not authenticator.is_loggedin :
        return redirect(url_for("login"))
    return render_template("home.html")

@app.get("/logout")
def logout():   
    authenticator.logout()
    return redirect(url_for("login"))

@app.post("/detect_faces")
def detect():
    return Response("bounding boxes", status=200)


if __name__ == "__main__":
    SESSION_TYPE = 'redis'
    SESSION_REDIS = Redis(host='localhost', port=6379)
    app.config.from_object(__name__)
    Session(app)
    app.run(debug=True, host="0.0.0.0",port="5000")
    