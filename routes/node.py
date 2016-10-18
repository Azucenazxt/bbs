from models.node import Node
from models.topic import Topic
from models.user import User

from routes import *



main = Blueprint('node', __name__)

Model = Node

@main.route('/')
@admin_required
def index():
    ms = Model.query.all()
    return render_template('node_index.html', node_list=ms)


@main.route('/<id>')
def show(id):
    u = current_user()
    m = Model.query.filter_by(id=id).first()
    if u is not None:
        return render_template('node_logined.html', node=m, user=u)
    else:
        return render_template('node.html', node=m)



@main.route('/edit/<id>')
@admin_required
def edit(id):
    m = Model.query.filter_by(id=id).first()
    return render_template('node_edit.html', node=m)


@main.route('/new/<id>')
@login_required
def new(id):
    u = current_user()
    m = Model.query.filter_by(id=id).first()
    if u is not None:
        return render_template('topic_new.html', node=m, user=u)
    else:
        return redirect(url_for('user.login_index'))


@main.route('/new')
@login_required
def new_topic():
    u = current_user()
    if u is not None:
        return render_template('t_new.html', user=u)
    else:
        return redirect(url_for('user.login_index'))


@main.route('/add', methods=['POST'])
def add():
    form = request.form
    m = Model(form)
    m.save()
    return redirect(url_for('.index'))


@main.route('/update/<id>', methods=['POST'])
def update(id):
    form = request.form
    m = Model.query.filter_by(id=id).first()
    m.update(form)
    return redirect(url_for('.index'))


@main.route('/delete/<id>')
@admin_required
def delete(id):
    m = Model.query.filter_by(id=id).first()
    m.delete()
    return redirect(url_for('.index'))
