from com.geo.service.googlegeo import GoogleGeoCoder
from com.geo.service.heregeo import HereGeoCoder
from com.geo.geoconfig import GeoConfig

class ServiceUtil():
    """The Service Factory take """
    config = GeoConfig()

    def getDefaultService(self):
        return self._getserviceInternal(True)

    def getFallbackService(self):
        return self._getserviceInternal(False)

    def _getserviceInternal(self, isdefault):
        for service_cfg in self.config.getConfig().services:
            if service_cfg.default is isdefault:
                if service_cfg.name == self.__class__.config.SERVICE_PROVIDER_GOOGLE:
                    return GoogleGeoCoder(service_cfg)
                elif service_cfg.name == self.__class__.config.SERVICE_PROVIDER_HERE and self._isServiceAvailabe(service_cfg):
                    return HereGeoCoder(service_cfg)
        return None

    def getservice(self, provider):
        """
        This method is used for returning a geoservice object by given the provider's name.
        :param provider:  the name of the service provider ("google" or "here")
        :return: the geoservice object

        Note: currently, this method is used for test only.
        """

        for service_cfg in self.__class__.config.getConfig():
            if provider == self.__class__.config.SERVICE_PROVIDER_GOOGLE:
                return GoogleGeoCoder(service_cfg)
            elif provider == self.__class__.config.SERVICE_PROVIDER_HERE and self._isServiceAvailabe(service_cfg):
                return HereGeoCoder(service_cfg)
        return None

    def _isServiceAvailabe(self, service_cfg):
        """Check to see if the service is available, my plug in project/environment specific strategy"""
        return True