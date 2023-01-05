from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, logout_user, LoginManager, current_user
from flask_migrate import Migrate
# from sqlalchemy import event
# import base64


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'secretkey123'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)

with app.app_context():
    db.create_all()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    notes = db.Column(db.Text)
    #files = db.Column(db.LargeBinary)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/')
def home():
    logout_user()
    return render_template('home.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    logout_user()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            login_user(user)
            return redirect(url_for('logged_in'))
        else:
            return render_template('login.html', error='Invalid username or password!')
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    logout_user()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password2 = request.form['password2']
        if password != password2:
            return render_template('register.html', error='Passwords must match! Please try again.')
        valid_user = User.query.filter_by(username=username).first()  # check if user with username provided exists
        if not valid_user:  # if does not exist create new user and add it to db
            user = User(username=username, password=password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'))
        else:
            return render_template('register.html', error='User with provided username already exists. Please choose other username!')
    return render_template('register.html')


@app.route('/logged_in', methods=['GET', 'POST'])
def logged_in():

    try:
        if request.method == 'POST':
            # update the notes for the logged in user
            current_user.notes = request.form['notes']
            #files = request.files.getlist('file')
            db.session.commit()
            #if files:
                #event.files = files[0].file.read()
        return render_template('logged_in.html', notes=current_user.notes)
    except AttributeError:
        return render_template('login.html', error='To access your notes you need to login first!')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


"""@app.route('/read')
def read():
    files = User.query.filter_by(id=User.id).first()
    encoded_image = base64.b64encode(files.img)
    return render_template('logged_in.html', files=encoded_image)"""


if __name__ == '__main__':
    app.run(debug=True)

