from models.topic import Topic
from models.node import Node
from models.user import User

from routes import *


main = Blueprint('topic', __name__)


Model = Topic


@main.route('/')
def index():
    ns = Node.query.all()
    ms = Model.query.all()
    u = current_user()
    if u is None:
        return render_template('bbs_index.html', node_list=ns, topic_list=ms)
    else:
        return render_template('bbs_logined_index.html', node_list=ns, topic_list=ms, user=u)


@main.route('/<id>')
def show(id):
    u = current_user()
    m = Model.query.filter_by(id=id).first()
    if u is not None:
        return render_template('topic_logined.html', topic=m, user=u)
    else:
        return render_template('topic.html', topic=m, user=u)


@main.route('/edit/<id>')
@login_required
def edit(id):
    m = Model.query.filter_by(id=id).first()
    return render_template('topic_edit.html', topic=m)


@main.route('/add', methods=['POST'])
@login_required
def add():
    form = request.form
    m = Model(form)
    m.node_id = int(form.get('node_id'))
    m.user_id = int(form.get('user_id'))
    m.save()
    return redirect(url_for('.index'))


@main.route('/update/<id>', methods=['POST'])
@login_required
def update(id):
    form = request.form
    m = Model.query.filter_by(id=id).first()
    m.update(form)
    return redirect(url_for('.index'))


@main.route('/delete/<id>')
@login_required
def delete(id):
    m = Model.query.filter_by(id=id).first()
    m.delete()
    return redirect(url_for('node.show', id=m.node_id))
