from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from flask_login import current_user
main_bp = Blueprint('main', __name__)
menu_bp = Blueprint('menu', __name__, url_prefix='/menu')

@main_bp.route('/')
@login_required
def index():
    return render_template('index.html', username=current_user.username)



@menu_bp.route('/manager')
def manager():
           return render_template('manger/user_manager.html')

@menu_bp.route('/anaylise')
def anaylise():
           return render_template('bar_example.html')
