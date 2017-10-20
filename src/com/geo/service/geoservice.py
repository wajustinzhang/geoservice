from abc import ABCMeta
from abc import abstractclassmethod

class GeoService:
    """
    The abstract class for all GeoService, it is used to provide service endpoint, request, response handling...

    """
    __metaclass__= ABCMeta
    def __init__(self, config):
        self.config = config

    @abstractclassmethod
    def getServiceUrl(self):
        raise NotImplementedError()

    @abstractclassmethod
    def formatResult(self, result, is_reverse):
        raise NotImplementedError()