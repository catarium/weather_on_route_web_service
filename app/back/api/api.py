from flask import Blueprint, request, jsonify
from app.services import accu_service
from app.services.weather_decision import is_weather_bad


# writing everything in one file, cuz there is no need for REST or stuff like that


router = Blueprint('api', __name__, url_prefix='/api')


@router.get('/weather')
def get_weather():
    kwargs = request.args
    start, end = kwargs.get('start', ''), kwargs.get('end', '')
    if not (start and end):
        return jsonify({'error': 'invalid args'}), 400

    start_location_key = accu_service.get_location_key(start)
    end_location_key = accu_service.get_location_key(end)
    err_msg = []
    if start_location_key is False or end_location_key is False:
        err_msg.append('accu error')
    if start_location_key == []  or end_location_key == []:
        err_msg.append('city not found')
    if err_msg:
        return jsonify({'error': err_msg}), 400

    start_weather = accu_service.get_weather(start_location_key)
    end_weather = accu_service.get_weather(end_location_key)
    print(start_weather)
    res = {
            'start': {
                'temp': start_weather[0]['Temperature']['Metric']['Value'],
                'wind': start_weather[0]['Wind']['Speed']['Metric']['Value'],
                'precipitation': start_weather[0]['HasPrecipitation'],
                'is_bad': is_weather_bad(start_weather[0]['Temperature']['Metric']['Value'],  
                                         start_weather[0]['Wind']['Speed']['Metric']['Value'],
                                         start_weather[0]['HasPrecipitation']
                )
                },
            'end': {
                'temp': end_weather[0]['Temperature']['Metric']['Value'],
                'wind': end_weather[0]['Wind']['Speed']['Metric']['Value'],
                'precipitation': end_weather[0]['HasPrecipitation'],
                'is_bad': is_weather_bad(end_weather[0]['Temperature']['Metric']['Value'],  
                                         end_weather[0]['Wind']['Speed']['Metric']['Value'],
                                         end_weather[0]['HasPrecipitation']
                )
                },
            }
    return jsonify(res)


