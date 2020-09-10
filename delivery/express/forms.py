from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, PasswordField
from wtforms.validators import DataRequired
import time


class boxForm(FlaskForm):
    box = StringField('快递单号', validators=[DataRequired()])
    submit = SubmitField('提交')


class deliveryForm(FlaskForm):
    id = StringField('快递单号', validators=[DataRequired()])
    name = StringField('姓名', validators=[DataRequired()])
    tel = StringField('电话号码', validators=[DataRequired()])
    time = SelectField('时间', choices=[time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))])
    status = SelectField('取件状态', choices=['未取件', '已取件'])
    submit = SubmitField('提交')


class findboxForm(FlaskForm):
    id = StringField('快递单号', validators=[DataRequired()])
    tel = StringField('电话号码', validators=[DataRequired()])
    submit = SubmitField('提交')


class loginForm(FlaskForm):
    name = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('提交')
