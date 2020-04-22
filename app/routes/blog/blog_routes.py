from flask import Blueprint, render_template, request, session
from app.helpers.loginHelper import is_logged_in
from app.dbModels.testimonals import testimonals
import datetime
from app import db

blog_bp = Blueprint('blog_bp', __name__, template_folder='app/templates')

@blog_bp.route('/blog', methods=['GET', 'POST'])
@is_logged_in
def blog():
    if request.method == 'POST':
        a = request
        feedback_result = testimonals(session['username'], request.form['comment'], request.form['rate'],
                                      datetime.datetime.now())
        db.session.add(feedback_result)
        db.session.commit()
    return render_template('blog.html')
