#!/usr/bin/env python3
""" Returns all students sorted by average score """


def top_students(mongo_collection):
    """
    Returns all students sorted by average score.,
    Args:
        mongo_collection: pymongo collection object.
    Returns:
        A list containing student documents with the average score.
    """
    sorted_students = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])

    return sorted_students
