import time
from functools import wraps
from typing import Callable, Type, Tuple


def retry(
    attempts: int = 3,
    delay: float = 1.0,
    exceptions: Tuple[Type[Exception], ...] = (Exception,),
):
    """
    Retry decorator.

    Args:
        attempts (int): Number of attempts before failing
        delay (float): Delay between retries in seconds
        exceptions (tuple): Exceptions to catch and retry

    Usage:
        @retry(attempts=3, delay=1)
        def my_function():
            ...
    """

    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None

            for attempt in range(1, attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    if attempt == attempts:
                        raise
                    time.sleep(delay)

            raise last_exception  # fallback safety

        return wrapper

    return decorator
