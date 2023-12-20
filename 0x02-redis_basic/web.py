#!/usr/bin/env python3
"""  requests module to obtain the HTML content
of a particular URL and returns it """

from functools import wraps

import redis
import requests

cache = redis.Redis()


def count_url_access(method):
    """
    Decorator to cache the result of a function
    with an expiration time of 10 seconds.
    """
    @wraps(method)
    def wrapper(url):
        cached_key = "cached:" + url
        cached_data = cache.get(cached_key)
        if cached_data:
            return cached_data.decode("utf-8")

        count_key = "count:" + url
        html = method(url)

        cache.incr(count_key)
        cache.set(cached_key, html)
        cache.expire(cached_key, 10)
        return html
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
