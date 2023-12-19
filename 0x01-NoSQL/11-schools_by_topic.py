#!/usr/bin/env python3
""" Returns the list of school having a specific topic """


def schools_by_topic(mongo_collection, topic):
    """
    List schools having a specific topic.
    Args:
        mongo_collection: pymongo collection object.
        topic (str): The topic to search for.
    Returns:
        A list containing school documents with the specified topic.
    """
    documents = mongo_collection.find({"topics": topic})
    list_docs = [d for d in documents]
    return list_docs
