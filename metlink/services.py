"""Stops (e.g.route 30) on the Metlink API."""

from ._util import _format_time


class MetlinkService(object):
    """A single service, e.g. Bus on route 1, from bus stop 1000."""

    def __init__(self, service_data):
        """Init with data from metlink api."""
        self._service_data = service_data

    @property
    def route_number(self):
        """Route number of this service."""
        return self._get('ServiceID')

    @property
    def departure_status(self):
        """Departure status of this service."""
        return self._get('DepartureStatus')

    @property
    def display_departure(self):
        """Display departure info for this service."""
        return _format_time(self._get('DisplayDeparture'))

    @property
    def is_real_time(self):
        """Real time info? (false if only scheduled)."""
        return self._get('IsRealtime')

    @property
    def origin_stop_name(self):
        """Stop where the services started."""
        return self._get('OriginStopName')

    @property
    def destination_stop_name(self):
        """Stop where the service will end."""
        return self._get('DestinationStopName')

    @property
    def departure_seconds(self):
        """Number of seconds until departure."""
        return self._get('DisplayDepartureSeconds')

    @property
    def departure_minutes(self):
        """Number of minutes until departure."""
        return int(self.departure_seconds / 60)

    @property
    def expected_departure(self):
        """Time the service is expected to depart."""
        value = self._get('ExpectedDeparture', False)
        if value:
            return _format_time(value)
        return value

    def attributes(self):
        """The Attributes of this service to give to HASS."""
        return {
            'Operator': self._get('OperatorRef'),
            'ExpectedDeparture': self.expected_departure,
            'DepartureStatus': self._get('DepartureStatus'),
            'IsRealtime': self._get('IsRealtime'),
            'OriginStopName': self._get('OriginStopName'),
            'DestinationStopName': self._get('DestinationStopName'),
            'VehicleFeature': self._get('VehicleFeature'),
            'ServiceID': self._get('ServiceID')
        }

    def _get(self, key, value=None):
        return self._service_data.get(key, value)

    def __str__(self):
        """String of the service_data."""
        return str(self._service_data)
