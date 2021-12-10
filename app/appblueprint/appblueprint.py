from flask import Blueprint, url_for, redirect

from forms import LoginForm, AddForm
from flask import flash, render_template
from models import User
from extensions import db, login_manager
from flask_login import login_user, logout_user

app_bp = Blueprint('rootbp', __name__)


@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)


@app_bp.route('/')
def index():
    return render_template('base.html')


@app_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.data['username']
        user = User.query.filter_by(username=username).first()
        login_user(user)
        flash('login success!')

    return render_template('login.html', form=form)


@app_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('rootbp.index'))


@app_bp.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()
    res = User.query.first()
    print(res)
    if form.validate_on_submit():
        data = form.data
        username = data['username']
        password = data['password']
        class_id = 10 * "一二三四五六".index(data['grd'][0]) + int(data['cls'][:-1])
        permission = ['学生', '班主任', '管理员'].index(data['role'])
        name = data['name']
        user = User(username=username, password=password, class_id=class_id, permission=permission, name=name)
        db.session.add(user)
        db.session.commit()
        flash('账户添加成功')


    return render_template('add.html', form=form)
