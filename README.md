# geoservice
## Design ideas
1   View controller uses Flask to handle web request/response, use service for REST service implementation
2   All geocode services are put in a definition file, config.json, default service and backup service are automatically handled by using the configuration definition
3:  Creating corresponding geo service ('google' and 'here') for any special request/response ... etc handling, in case there are different support and format from differewnt vendor (Note: after implementation, there is no different for current two simple APIs. this design is just for scalability)  
4: TDD

## 1 Details of the implementation
### 1.1 Source code
Source code under 'src' folder

1. geocodecontroller.py -- this is the REST web service class. it provide two rest service as in following examples:

http://127.0.0.1:5000/coordinate?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA
http://127.0.0.1:5000/address?latlng=37.4216548,%20-122.0856374

Inside geocodecontroller.py, two service are used:
Flask to handle web request/response
Service object for implementation.

2. service.py -- the service class which is used by geocodecontroller.py to implement the web services

3. serviceutil.py -- the service utility method to return the default service and the backup service.

4. geo services
1) geoservice.py --- The service base class
2) googlegeo.py (extends geoservice) --- geoservice to handle google specific request/response ...etc
3) heregeo.py (extends geoservice) --- geoservice to handle here specific request /response ... etc
   
5: configuration
1) config.json -- the json file to put definition of all backend service
2) the geoconfig.py -- runtime object for config.json

### Test code
Test code are under 'test' folder

## 2 Run the code
### 2.1 Development
  Checkout the code, open in pyCharm, run geocodecontroller.py
  Run through unittests

### 2.2 Deployment
  TODO

## 3. Tasks to do
1: Introduce auth support
2: More document and tests

