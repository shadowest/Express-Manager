from flask import Blueprint, flash, render_template
from express.forms import *
from express.models import *
user = Blueprint('user', __name__, template_folder='templates/user')


@user.route('/user', methods=['GET', 'POST'])
def findbox():
    findbox_form = findboxForm()
    row_id = []
    if findbox_form.validate_on_submit():
        id = findbox_form.id.data
        tel = findbox_form.tel.data
        state = Delivery.query.filter(Delivery.ID == id).first()
        if state is None:
            flash("该快递单号不存在")
        else:
            id_tel = state.TEL
            if tel != id_tel:
                flash('快递单号和电话号码不匹配')
            else:
                state = Delivery.query.filter(Delivery.ID == id).first()
                row_x = [state.ID, state.NAME, state.TEL, state.Time, state.Status]
                row_id.append(id)
                return render_template("user/user.html", form=findbox_form, row=row_x, row_id=row_id)
    return render_template('user/user.html', form=findbox_form)