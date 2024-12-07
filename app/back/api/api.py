from flask import Blueprint


# writing everything in one file, cuz there is no need for REST or stuff like that


router = Blueprint('api', __name__, url_prefix='/api')


@router.get('/city')
def get_city():
    pass


@router.get('/weather')
def get_weather():
    pass


