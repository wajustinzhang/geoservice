import unittest
from com.geo.geoconfig import GeoConfig

class TestGeoCodeController(unittest.TestCase):
    def setUp(self):
        self.cfg = GeoConfig()

    def test_getConfig(self):
        result = self.cfg.getConfig()
        assert result.__len__() > 0

    if __name__ == '__main__':
        unittest.main()
