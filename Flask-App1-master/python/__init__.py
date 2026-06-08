from flask import Flask
from python.config import Config
from python.extensions import db, login_manager, bootstrap

def create_app(config_class=Config):
    app = Flask(__name__, template_folder='../web/templates')
    app.config.from_object(config_class)

    # 初始化扩展
    db.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)

    # 注册蓝图
    from python.control.auth_controller import auth_bp
    from python.control.view_controller import main_bp
    from python.control.view_controller import menu_bp
    from python.control.user_controller import manger_bp
    from python.control.anallise_controller import anallise_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(manger_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(menu_bp)
    app.register_blueprint(anallise_bp)


    return app
