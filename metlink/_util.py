"""Private utils used by this module."""
from datetime import timedelta, datetime


def _format_time(t):
    """Create times that match those seen on the street signs."""
    ret = datetime.strptime(t[0:16], '%Y-%m-%dT%H:%M')
    if t[18] == '+':
        ret += timedelta(hours=int(t[19:22]), minutes=int(t[23:]))
    elif t[18] == '-':
        ret -= timedelta(hours=int(t[19:22]), minutes=int(t[23:]))

    return ret.strftime("%I:%M%p %a")
