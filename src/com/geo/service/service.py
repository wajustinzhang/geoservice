import requests
from com.geo.service.serviceUtil import ServiceUtil

class Service:
    """This is the GeoService base template, serving as the super class for each individual service like the
    googlegeo service and heregeo service as implemented in this sample. """

    def __init__(self):
        """Here to initialize state related to service calls"""
        pass

    def getCoordinate(self, address):
        """
        This method is to return the corresponding coordinate from the pass-in address information

        :param address: the passing address, for example 123 kelly stree, san francisco, ca
        :return: a list of coordinates from the geocoding service return for that address.
        """

        params = "address={address}".format(address=address)
        geoService = ServiceUtil().getDefaultService()
        service_ep = geoService.getServiceUrl()
        url = '{base}&{params}'.format(base=service_ep, params=params)
        return self.__servicecall__(geoService, url, params, False)

    def getAddress(self, coordinate):
        """
        This method is to return the corresponding addresses from the pass-in coordinate information

        :param coordinate: the coordinate information, in format of {'latitude':lvalue, 'longitude':lgvalue}
        :return: the address list to the coordinate.
        """
        params = "latlng={lat},{lon}".format(lat=coordinate['latitude'], lon=coordinate['longitude'])
        service = ServiceUtil().getDefaultService()
        service_ep = service.getServiceUrl()
        url = '{base}&{params}'.format(base=service_ep, params=params)
        return self.__servicecall__(service, url, params, True)

    def __servicecall__(self, geoService, url, params, isreverse):
        response = requests.get(url)
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            # if debug mode
            # print(str(e))
            geoService = ServiceUtil().getFallbackServiceUrl()
            url = '{base}&{params}'.format(base=geoService.getServiceUrl(), params=params)
            response = requests.get(url)
            try:
                response.raise_for_status()
            except requests.exceptions.HTTPError as he:
                print(str(he))

        return geoService.formatResult(response.json(), isreverse)