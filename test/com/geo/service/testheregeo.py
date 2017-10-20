import unittest
from com.geo.service.serviceUtil import ServiceUtil

class TestHereGeo(unittest.TestCase):
    def setUp(self):
        self.service = ServiceUtil().getservice("here")

    def test_getServiceUrl(self):
        result = self.service.getServiceUrl()
        assert result.index('here') > 0

    def test_formatResult(self):
        pass

    if __name__ == "__main__":
        unittest.main()
