from flask import Blueprint, render_template


router = Blueprint(name='back', import_name=__name__, template_folder='templates', url_prefix='', root_path='.')


@router.get('/')
def home_page():
    return render_template('home.html')
