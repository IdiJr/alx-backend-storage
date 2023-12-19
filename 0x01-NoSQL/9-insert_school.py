#!/usr/bin/env python3
"""
Inserts a new document in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a MongoDB collection based on kwargs.
    Args:
        mongo_collection: pymongo collection object.
        **kwargs: Key-value pairs representing the fields
        and values for the new document.
    Returns:
        The new _id of the inserted document.
    """
    document_id = mongo_collection.insert(kwargs)
    return document_id
