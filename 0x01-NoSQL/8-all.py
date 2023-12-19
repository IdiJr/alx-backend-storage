#!/usr/bin/env python3
"""
Lists all documents in a collection
"""


def list_all(mongo_collection):
    """ Lists all documents in a MongoDB collection
        Args:
            mongo_collection: pymongo collection object.
        Returns:
            A list containing all documents in the collection.
            Returns an empty list if no documents are found.
    """
    all_documents = []
    documents = mongo_collection.find({})

    for document in documents:
        all_documents.append(document)

    return all_documents
