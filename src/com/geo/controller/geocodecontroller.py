from flask import Flask, request, Response
from flask import jsonify

from com.geo.controller.geoexception import GeoException
from com.geo.service.service import Service

app = Flask(__name__)
service = Service()

"""
   Web Rest Interface.
"""

@app.route('/')
def api_root():
    return 'Welcome to the home page of sample geocoding rest service'

@app.route('/address')
def getAddress():
    if 'latlng' in request.args:
        latlng = request.args['latlng'].split(",")
        coordinate = {'latitude':latlng[0], 'longitude':latlng[1]}
        result = service.getAddress(coordinate)
        resp = Response(result, status=200, mimetype='application/json')
        return resp
    else:
        raise GeoException('no latlng query in request')

@app.route('/coordinate')
def getCoordinate():
    if 'address' in request.args:
        address = request.args['address']
        result = service.getCoordinate(address)
        response = jsonify(result)
        response.status_code = 200
        return response
    else:
        raise GeoException('no address query in request')

# =============== error handling ================
@app.errorhandler(GeoException)
def handle_geo_service_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

if __name__ == '__main__':
    app.run()