import datetime
from typing import Optional, Union


def get_current_time(fmt: str = "%Y-%m-%d %H:%M:%S",
                     tz: Optional[datetime.tzinfo] = None) -> str:
    """
    Returns the current time as a formatted string.

    :param fmt: Format string compliant with datetime.strftime.
    :param tz: Optional timezone information.
    :return: Formatted current time.
    """
    now = datetime.datetime.now(tz)
    return now.strftime(fmt)


def get_timestamp(tz: Optional[datetime.tzinfo] = None) -> float:
    """
    Returns the current time as a timestamp (seconds since epoch).

    :param tz: Optional timezone information.
    :return: Timestamp.
    """
    return datetime.datetime.now(tz).timestamp()


def parse_time(time_str: str, fmt: str = "%Y-%m-%d %H:%M:%S") -> datetime.datetime:
    """
    Parses a time string into a datetime object.

    :param time_str: string representation of time.
    :param fmt: format of the input string.
    :return: datetime object.
    """
    return datetime.datetime.strptime(time_str, fmt)


if __name__ == "__main__":
    # Example usage
    print("Current Time:", get_current_time())
