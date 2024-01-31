from flask import Flask, render_template, url_for, redirect, request
from pip._vendor import requests
from flask_bcrypt import Bcrypt
from sqlalchemy.sql import func
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, RadioField, DateField
from wtforms.validators import InputRequired, Length, ValidationError

app = Flask(__name__)
bcrypt = Bcrypt(app)
API_KEY = 'S1HTWWB10I1LB5VA'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/antarag/Desktop/budgetary-flask/database.db'
app.config['SECRET_KEY'] = 'thisisasecretkey'
db = SQLAlchemy(app)
app.app_context().push()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String(300), nullable=False)
    date = db.Column(db.String(300), nullable=False)
    link = db.Column(db.String(300), nullable=False)

class RegisterForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Register')

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
            username=username.data).first()
        if existing_user_username:
            raise ValidationError(
                'That username already exists. Please choose a different one.')


class LoginForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')

class CreateNewArticle(FlaskForm):
    title = StringField('Article Title', validators=[InputRequired(), Length(max=100)])
    author = StringField('Author', validators=[InputRequired(), Length(max=30)])
    desc = TextAreaField('Description', validators=[InputRequired(), Length(max=100)])
    date = DateField('Date', validators=[InputRequired()])
    link = StringField('Link', validators=[InputRequired(), Length(max=200)])
    submit = SubmitField('Create')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('view_articles'))
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html', form=form)

@app.route('/new_article', methods=['GET', 'POST'])
@login_required
def new_article():
    form = CreateNewArticle()
    if form.validate_on_submit():
        new_article = Article(title=form.title.data, author=form.author.data, desc=form.desc.data, date=form.date.data, link=form.link.data)
        db.session.add(new_article)
        db.session.commit()
        return redirect(url_for('view_articles'))
    return render_template('add_article.html', form=form)

@app.route('/view_articles')
@login_required
def view_articles():
    articles = Article.query.order_by(Article.id.desc()).limit(20).all()
    return render_template('view_articles.html', articles = articles)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/activities')
def activities():
    return render_template('activities.html')

@app.route('/activities/compound-simple-interest')
def activity1():
    return render_template('activity1.html')

@app.route('/activities/compound-interest-calculator')
def activity2():
    return render_template('activity2.html')

@app.route('/activities/forex-calculator', methods=['GET', 'POST'])
def activity3():
    if request.method == 'POST':
        try:
            amount = request.form['amount']
            amount = float(amount)
            from_c = request.form['from_c']
            to_c = request.form['to_c']
            url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={}&to_currency={}&apikey={}'.format(
                from_c, to_c, API_KEY)
            response = requests.get(url=url).json()
            rate = response['Realtime Currency Exchange Rate']['5. Exchange Rate']
            rate = float(rate)
            result = rate * amount
            from_c_code = response['Realtime Currency Exchange Rate']['1. From_Currency Code']
            from_c_name = response['Realtime Currency Exchange Rate']['2. From_Currency Name']
            to_c_code = response['Realtime Currency Exchange Rate']['3. To_Currency Code']
            to_c_name = response['Realtime Currency Exchange Rate']['4. To_Currency Name']
            time = response['Realtime Currency Exchange Rate']['6. Last Refreshed']
            return render_template('activity3.html', result=round(result, 2), amount=amount,
                                   from_c_code=from_c_code, from_c_name=from_c_name,
                                   to_c_code=to_c_code, to_c_name=to_c_name, time=time)
        except Exception as e:
            return '<h1>Bad Request : {}</h1>'.format(e)
  
    else:
        return render_template('activity3.html')

@app.route('/activities/savings-target-calculator')
def activity4():
    return render_template('activity4.html')

@app.route('/activities/sip-calculator')
def activity5():
    return render_template('activity5.html')

@app.route('/tools')
def tools():
    return render_template('tools.html')

@app.route('/blogs')
def blogs():
    articles = Article.query.order_by(Article.id.desc()).all()
    print(articles)
    return render_template('blogs.html', articles=articles)




@app.route('/<int:article_id>/edit/', methods=('GET', 'POST'))
def edit(article_id):
    article = Article.query.get_or_404(article_id)
    print(type(article))
    if request.method == 'POST':
            title = request.form['title']
            author = request.form['author']
            desc = request.form['desc']
            date = request.form['date']
            link = request.form['link']

            article.title = title
            article.author = author
            article.desc = desc
            article.date = date
            article.link = link

            db.session.add(article)
            db.session.commit()

            return redirect(url_for('blogs'))
    
    return render_template('edit.html', article=article)

if __name__ == "__main__":
    app.run(port=8000, debug=True)