import json
import os
from collections import namedtuple


class GeoConfig:
    """The config file for reading & processing config information defined inside config.json"""
    SERVICE_PROVIDER_GOOGLE = 'google'
    SERVICE_PROVIDER_HERE = 'here'
    cfg = {}

    def __init__(self):
        dir = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        with open(os.path.join(dir, 'config.json'), 'r') as configfile:
            data = configfile.read()
            self.__class__.cfg = json.loads(data, object_hook=lambda d: namedtuple('config', d.keys())(*d.values()))
            configfile.close()

    def getConfig(self):
        return self.__class__.cfg