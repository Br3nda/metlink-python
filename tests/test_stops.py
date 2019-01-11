import unittest

from metlink import MetlinkStop

class MetlinkStopTest(unittest.TestCase):
    def test_fetch(self):
        metlink_stop = MetlinkStop.fetch(3704)

        self.assertEqual(metlink_stop.stop_name, 'Woodridge Drive at Glenwood Grove (near 19)')
        self.assertEqual(metlink_stop.longitude, 174.8314677)
        self.assertEqual(metlink_stop.latitude, -41.2197591)


if __name__ == '__main__':
    unittest.main()
