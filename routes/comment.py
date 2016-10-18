from models.node import Node
from models.topic import Topic
from models.comment import Comment
from routes import *


main = Blueprint('comment', __name__)

Model = Comment


@main.route('/add', methods=['POST'])
@login_required
def add():
    form = request.form
    m = Model(form)
    m.topic_id = int(form.get('topic_id'))
    m.user_id = int(form.get('user_id'))
    m.save()
    return redirect(url_for('topic.show', id=m.topic_id))


# @main.route('/delete/<id>')
# def delete(id):
#     m = Model.query.filter_by(id=id).first()
#     m.delete()
#     return redirect(url_for('.index'))
