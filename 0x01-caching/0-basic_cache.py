#!/usr/bin/env python3
"""
This module contains the BasicCache class which inherits from the BaseCaching class.
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache defines a caching system without any limit """

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
