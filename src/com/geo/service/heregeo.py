from com.geo.service.geoservice import GeoService

class HereGeoCoder(GeoService):
    def __init__(self, config):
        super(HereGeoCoder, self).__init__(config)

    def getServiceUrl(self):
        return self.config.endpoint.url + '?app_id=' + self.config.endpoint.app_id + '&app_code=' + self.config.endpoint.app_code

    def formatResult(self, result, isreverse):
        records = []
        for record in result['results']:
            if isreverse:
                records.append(record['formatted_address'])
            else:
                records.append((record['geometry']['location']['lat'], record['geometry']['location']['lng']))
        return records[0]