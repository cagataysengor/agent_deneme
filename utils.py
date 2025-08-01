import datetime
from typing import Optional

def get_current_time(fmt: str = "%Y-%m-%d %H:%M:%S", tz: Optional[datetime.tzinfo] = None) -> str:
    """
    Return the current time formatted according to the given format string.

    Args:
        fmt (str): Format string compatible with datetime.strftime. Defaults to "%Y-%m-%d %H:%M:%S".
        tz (Optional[datetime.tzinfo]): Time zone info. If None, system local time is used.

    Returns:
        str: Formatted current time.
    """
    now = datetime.datetime.now(tz)
    return now.strftime(fmt)


def get_timestamp() -> float:
    """
    Return the current time as a UNIX timestamp (seconds since the epoch).

    Returns:
        float: Current UNIX timestamp.
    """
    return datetime.datetime.now().timestamp()


def parse_time(time_str: str, fmt: str = "%Y-%m-%d %H:%M:%S") -> datetime.datetime:
    """
    Parse a time string according to the given format and return a datetime object.

    Args:
        time_str (str): Time string to parse.
        fmt (str): Format string compatible with datetime.strptime.

    Returns:
        datetime.datetime: Parsed datetime object.
    """
    return datetime.datetime.strptime(time_str, fmt)
