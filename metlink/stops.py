"""Stops (e.g. bus stops, stations) on the Metlink API."""

import requests

from .services import MetlinkService

_STOP_URL = "https://www.metlink.org.nz/api/v1/StopDepartures/{stop_number}"


class MetlinkStop(object):
    """A bus stop or train station."""

    @classmethod
    def fetch(cls, stop_number):
        """Retrieve stop into from metlink's API."""
        url = _STOP_URL.format(stop_number=stop_number)
        r = requests.get(url)
        return MetlinkStop(r.json())

    def __init__(self, data):
        """Init with data from the metlink API."""
        self._data = data

    def services(self, route_number=None):
        """List of services expected at the stop."""
        for data in self._data.get('Services'):
            service = MetlinkService(data)
            if str(route_number) == str(service.route_number):
                yield service

    @property
    def stop_name(self):
        """Name of the stop."""
        return self._data.get('Stop', {}).get('Name')

    @property
    def longitude(self):
        """Longitude of the stop's location."""
        return self._data.get('Stop', {}).get('Long')

    @property
    def latitude(self):
        """Latitude of the stop's location."""
        return self._data.get('Stop', {}).get('Lat')

    def next_service(self, route_number=None):
        """The next service expected to arrive here."""
        # optionally filtered by route_number
        for service in self.services(route_number=route_number):
            return service
