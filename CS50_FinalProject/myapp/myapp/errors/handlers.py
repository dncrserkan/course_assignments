from flask import render_template, flash, Blueprint


errors = Blueprint('errors', __name__)


@errors.app_errorhandler(404)
def error_404(error):
    flash('Page Not Found (404)', 'warning')
    return render_template('errors/404.html'), 404  
    # second (404) is status code default is 200


@errors.app_errorhandler(403)
def error_403(error):
    flash("You don't have permission to do that (403)", 'warning')
    return render_template('errors/403.html'), 403


@errors.app_errorhandler(500)
def error_500(error):
    flash('Something went wrong (500)', 'warning')
    return render_template('errors/500.html'), 500 
