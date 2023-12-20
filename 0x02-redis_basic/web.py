#!/usr/bin/env python3
"""  requests module to obtain the HTML content
of a particular URL and returns it """

import requests
import redis
from functools import wraps

cache = redis.Redis()


def count_url_access(method):
    """
    Decorator to cache the result of a function
    with an expiration time of 10 seconds.
    """
    @wraps(method)
    def wrapper(url: str) -> str:
        key = f"count:{url}"
        count = cache.get(key)
        if count is None:
            count = 0
        count += 1
        cache.set(key, count, ex=10)

        result_key = f"result:{url}"
        cached_result = cache.get(result_key)
        if cached_result is not None:
            return cached_result.decode()

        result = method(url)
        cache.set(result_key, result, ex=10)
        return result
    return wrapper


@count_url_access
def get_page(url: str) -> str:
    """
    Retrieve the HTML content of a particular URL and cache the result.
    Args:
        url (str): The URL to retrieve the HTML content from.
    Returns:
        str: The HTML content of the URL.
    """
    response = requests.get(url)
    return response.text
