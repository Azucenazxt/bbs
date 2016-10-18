from models.user import User
from routes import *


main = Blueprint('user', __name__)

Model = User

@main.route('/register/index')
def register_index():
    return render_template('user_register.html')


@main.route('/login/index')
def login_index():
    return render_template('user_login.html')


@main.route('/register', methods=['POST'])
def register():
    form = request.form
    m = Model(form)
    message = m.valid_register()
    if message[0]:
        m.save()
    msgs = message[1]
    return render_template('user_register.html', msgs=msgs)


@main.route('/login', methods=['POST'])
def login():
    form = request.form
    m = Model(form)
    message = m.valid_login()
    if message[0]:
        return redirect(url_for('topic.index'))
    else:
        msgs = message[1]
    return render_template('user_login.html', msgs=msgs)


@main.route('/out')
def login_out():
    session.pop('user_id')
    return redirect(url_for('topic.index'))

@main.route('/settings')
def set():
    u = current_user()
    return render_template('user_setting.html', user=u)

@main.route('/update', methods=['POST'])
def update():
    u = current_user()
    m = Model.query.filter_by(id=u.id).first()
    form = request.form
    new_m = Model(form)
    m.title = new_m.title
    m.save()
    return render_template('user_setting.html', user=m)


@main.route('/new/password', methods=['POST'])
def change_password():
    old_password = request.form.get('password')
    new_password = request.form.get('new_password')
    renew_password = request.form.get('renew_password')
    u = current_user()
    m = Model.query.filter_by(id=u.id).first()
    if m.password == old_password and new_password == renew_password:
        m.password = new_password
        m.save()
    return render_template('user_setting.html', user=m)

