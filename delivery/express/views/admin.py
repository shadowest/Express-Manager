from flask import Blueprint, flash, render_template, redirect, url_for
from express.forms import *
from express.models import *
from express.utils import redirect_back

administrator = Blueprint('admin', __name__, template_folder='templates/admin')


@administrator.route('/find', methods=['GET', 'POST'])
def find():
    box_form = boxForm()
    id = []
    if box_form.validate_on_submit():
        box_id = box_form.box.data
        state = Delivery.query.filter(Delivery.ID == box_id).first()
        if state is None:
            flash("该快递单号不存在")
        else:
            id.append(state.ID)
            row_x = [state.ID, state.NAME, state.TEL, state.Time, state.Status]
            return render_template("admin/find.html", form=box_form, row=row_x, row_id=id)
    return render_template("admin/find.html", form=box_form)


@administrator.route('/admin')
def admin():
    return render_template('admin/admin.html')


@administrator.route("/login", methods=["POST", "GET"])
def login():
    login_form = loginForm()
    if login_form.validate_on_submit():
        name = login_form.name.data
        password = login_form.password.data
        if name == 'admin' and password == 'admin':
            return redirect(url_for('admin.admin'))
        else:
            flash('用户名或密码错误!')
    return render_template('admin/login.html', form=login_form)


@administrator.route('/addbox', methods=['GET', 'POST'])
def addbox():
    delivery_form = deliveryForm()
    delivery_id = []
    if delivery_form.validate_on_submit():
        id = delivery_form.id.data
        name = delivery_form.name.data
        tel = delivery_form.tel.data
        time = delivery_form.time.data
        status = delivery_form.status.data

        flag = Delivery.query.filter_by(ID=id).first()

        if flag is not None:
            flash("输入错误，该订单号已存在，请重新输入")
        else:
            new_delivery = Delivery(ID=id, NAME=name, TEL=tel, Time=time, Status=status)
            db.session.add(new_delivery)
            db.session.commit()
            flash("提交成功")
            delivery_row = [id, name, tel, time, status]
            delivery_id.append(id)
            return render_template("admin/addbox.html", form=delivery_form, row=delivery_row, row_id=delivery_id)
    return render_template("admin/addbox.html", form=delivery_form)


@administrator.route('/list')
def list():
    rows = Delivery.query.all()
    return render_template("admin/list.html", rows=rows)


@administrator.route('/delete/<id>')
def delete(id):
    id_flag = Delivery.query.filter_by(ID=id).first()
    if id_flag is not None:
        result = Delivery.query.filter(Delivery.ID == id).first()
        db.session.delete(result)
        db.session.commit()
        flash('成功删除快递信息')
    else:
        flash("找不到该快递")
    return redirect_back('/delete/<id>')


@administrator.route('/change/<id>')
def change(id):
    state = Delivery.query.filter(Delivery.ID == id).first()
    if state.Status == '已取件':
        flash('该快递已被去除，请勿重复取件')
    else:
        state.Status = '已取件'
        db.session.commit()
        flash('成功取出该快递')
    return redirect_back('/change/<id>')
