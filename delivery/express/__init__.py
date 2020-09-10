from flask import Flask, render_template, session
from .models import *
from .forms import *
from .utils import *
from .config import Config
from .views.user import user
from .views.admin import administrator

# 初始化
app = Flask(__name__)
app.config.from_object(Config)
app.app_context().push()
db.init_app(app)
db.create_all()
app.register_blueprint(administrator)
app.register_blueprint(user)


@app.route('/')
def homepage():
    return render_template('home.html')


# @app.route("/logout")
# def logout():
#     session.pop('username', None)
#     session.pop('password', None)
#     return redirect(url_for('homepage'))








