from flask import Blueprint


router = Blueprint('back', __name__, template_folder='templates', url_prefix='/tasks')
