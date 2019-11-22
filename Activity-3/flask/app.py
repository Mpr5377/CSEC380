from flask import Flask, flash, render_template, request, session, redirect, url_for
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import pymysql, datetime, time, os
from werkzeug import generate_password_hash, check_password_hash

# Wait
time.sleep(30)

# Flask app
app = Flask(__name__, static_url_path='/static', template_folder='templates')

# Rate limit

limiter = Limiter (
    app,
    key_func=get_remote_address,
    default_limits=["28000 per day", "1000 per hour", "20 per minute"]
)
# Creating Sessions
secretKey = os.urandom(24)
app.secret_key = secretKey


# Connect to MYSQL
mysqlConn= pymysql.connect('mysql', 'root', 'root', 'db')
mysqlConnCursor = mysqlConn.cursor()

# Create users
user1 = 'admin'
user1hashedpass = generate_password_hash('admin')
mysqlConnCursor.execute("INSERT INTO users(Username, HashedPass, VideoCount, CreationDate) VALUES ('{}', '{}', 0, '{}')".format(user1, user1hashedpass, datetime.datetime.now().strftime('%Y-%m-%d')))
mysqlConnCursor.close()
mysqlConn.commit()
mysqlConn.close()


@app.route("/")
def home():
    return render_template('login.html')


@app.route("/login", methods=['GET','POST'])
@limiter.limit("14400/day;600/hour;10/minute")
def login():
    mysqlConn= pymysql.connect('mysql', 'root', 'root', 'db')
    mysqlConnCursor = mysqlConn.cursor()
    if request.method == 'GET':
        return home()
    username = request.form['username']
    password = request.form['password']
    hashedpass = generate_password_hash(password)
    mysqlConnCursor.execute("SELECT HashedPass FROM users WHERE Username="+"'"+str(username)+"'")
    userpass = mysqlConnCursor.fetchone()
    mysqlConnCursor.close()
    mysqlConn.close()
    if userpass == None:
        return invalid_user()
    elif check_password_hash(userpass[0], password):
        session['username'] = username
        return redirect(url_for('homepage'))
    return invalid_password()

@app.route("/logout", methods=['GET','POST'])
def logout():
    session.pop('username', None)
    flash('You were logged out.')
    return redirect(url_for('login'))

@app.route("/upload", methods=['GET','POST'])
def upload():
    if 'username' in session:
        return render_template('view.html', username = session['username'])
    return render_template('login.html')


@app.route("/view")
def view():
    if 'username' in session:
        return render_template('upload.html', username=session['username'])
    return render_template('login.html')



@app.route("/invalid_user")
def invalid_user():
    return """
        <!DOCTYPE html>
    <html>
    <head>
      <title>Invalid Username</title>
    </head>
      <body>The username used does not exist</body>
    </html>
    """


@app.route("/invalid_password")
def invalid_password():
    return """
        <!DOCTYPE html>
    <html>
    <head>
      <title>Invalid password</title>
    </head>
      <body>Invalid password</body>
    </html>
    """


@app.route("/home", methods=['GET','POST'])
def homepage():
    if 'username' in session:
        return render_template('home.html', username = session['username'])
    else:
        return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(host='0.0.0.0')
