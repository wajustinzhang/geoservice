from abc import ABCMeta
from abc import abstractclassmethod

class GeoService:
    """
    The abstract class for all GeoServices, it provides methods for specific handling in each GeoService with respect to
    service endpoint, request, response
    """
    __metaclass__= ABCMeta
    def __init__(self, config):
        """
        Each GeoService has a corresponding configuration definition (from config.json)
        :param config: the configuration object for the GeoService
        """
        self.config = config

    @abstractclassmethod
    def getServiceUrl(self):
        """
        Abstract method. implemented by sub class
        :return:
        """
        raise NotImplementedError()

    @abstractclassmethod
    def formatResult(self, result, is_reverse):
        """
        Abstract method. implemented by sub class
        :return:
        """
        raise NotImplementedError()