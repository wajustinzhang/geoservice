import unittest
from com.geo.service.service import Service

class TestService(unittest.TestCase):
    def setUp(self):
        self.service = Service()

    def test_getAddress(self):
        address = "137 Lyndhurst Pl, San Ramon, CA"
        result = self.service.getCoordinate(address)
        assert result is not None and len(result) > 0

    def test_getCoordinate(self):
        coordinate = {}
        coordinate['latitude'] = 37.7566725
        coordinate['longitude'] = -121.9986352
        result = self.service.getAddress(coordinate)
        assert result is not None and len(result) > 0

    if __name__ == "__main__":
        unittest.main()