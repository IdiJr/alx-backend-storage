#!/usr/bin/env python3
""" Changes all topics of a school document based on the name """


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name.
    Args:
        mongo_collection: pymongo collection object.
        name (str): The school name to update.
        topics (list): The list of topics to set for the school.
    Returns:
        None
    """
    query = {"name": name}
    new_values = {"$set": {"topics": topics}}

    mongo_collection.update_many(query, new_values)
