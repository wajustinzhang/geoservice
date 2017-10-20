from com.geo.service.geoservice import GeoService

class GoogleGeoCoder(GeoService):
    """
      Google Geoservice. placeholder for all google GeoCoding service details.
    """
    def __init__(self, config):
        super(GoogleGeoCoder, self).__init__(config)

    def getServiceUrl(self):
        """
        :return: the service endpoint which is used to config service request along with pass-in params
        """
        return self.config.endpoint.url + '/' + self.config.endpoint.format + '?key=' + self.config.endpoint.api_key

    def formatResult(self, result, isCoordinate):
        """
        :param result: return from google Geo service request
        :param isCoordinate: if the result is coordinate.
        :return:  the formated result for service API (TODO here only for two web service API (getAddress() and
         getCoorindate() in services, may need to expand if needed)
        """
        records = []
        for record in result['results']:
            if isCoordinate:
                records.append(record['formatted_address'])
            else:
                records.append((record['geometry']['location']['lat'], record['geometry']['location']['lng']))
        if len(records) > 0:
            return records[0]

        return None
