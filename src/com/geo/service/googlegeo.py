from com.geo.service.geoservice import GeoService

class GoogleGeoCoder(GeoService):
    def __init__(self, config):
        super(GoogleGeoCoder, self).__init__(config)

    def getServiceUrl(self):
        return self.config.endpoint.url + '/' + self.config.endpoint.format + '?key=' + self.config.endpoint.api_key

    def formatResult(self, result, isreverse):
        records = []
        for record in result['results']:
            if isreverse:
                records.append(record['formatted_address'])
            else:
                records.append((record['geometry']['location']['lat'], record['geometry']['location']['lng']))
        return records[0]
