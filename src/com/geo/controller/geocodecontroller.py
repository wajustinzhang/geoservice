from flask import Flask, request, json, Response
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

    return Response("error", status=200, mimetype='application/json')

@app.route('/coordinate')
def getCoordinate():
    if 'address' in request.args:
        address = request.args['address']
        result = service.getCoordinate(address)
        resp = Response(str(result), status=200, mimetype='application/json')
        return resp

    return Response("error", status=400, mimetype='application/json')

if __name__ == '__main__':
    app.run()