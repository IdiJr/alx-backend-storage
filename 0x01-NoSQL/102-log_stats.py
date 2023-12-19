#!/usr/bin/env python3
""" Provides some stats about Nginx logs stored in MongoDB """
from pymongo import MongoClient

METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def count_logs(mongo_collection):
    """
    Count the number of logs in the MongoDB collection.
    Args:
        mongo_collection: pymongo collection object.
    Returns:
        The number of documents in the collection.
    """
    return mongo_collection.count_documents({})


def count_methods(mongo_collection, methods):
    """
    Count the number of logs for each specified method.
    Args:
        mongo_collection: pymongo collection object.
        methods (list): List of HTTP methods to count.
    Returns:
        A dictionary containing the count for each method.
    """
    method_counts = {}
    for method in methods:
        method_counts[method] = mongo_collection.count_documents(
            {"method": method})
    return method_counts


def count_status_check(mongo_collection, path):
    """
    Count the number of logs with a specific path.
    Args:
        mongo_collection: pymongo collection object.
        path (str): The path to count.
    Returns:
        The count of logs with the specified path.
    """
    return mongo_collection.count_documents({"path": path})


def top_ips(mongo_collection, limit=10):
    """
    Get the top 10 most present IPs in the MongoDB collection.
    Args:
        mongo_collection: pymongo collection object.
        limit (int): Number of top IPs to retrieve.
    Returns:
        A list of tuples containing IP and count, sorted by count.
    """
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": limit}
    ]
    result = mongo_collection.aggregate(pipeline)

    return [(entry["_id"], entry["count"]) for entry in result]


def log_stats(mongo_collection):
    """
    Print log statistics from the MongoDB collection.
    Args:
        mongo_collection: pymongo collection object.
    """
    total_logs = count_logs(mongo_collection)
    print(f"{total_logs} logs")

    method_counts = count_methods(mongo_collection, METHODS)
    print("Methods:")
    for method, count in method_counts.items():
        print(f"\tmethod {method}: {count}")

    status_check_count = count_status_check(mongo_collection, path="/status")
    print(f"{status_check_count} status check")

    top_ips_list = top_ips(mongo_collection, limit=10)
    print("IPs:")
    for ip, count in top_ips_list:
        print(f"\t{ip}: {count}")


if __name__ == "__main__":
    nginx_collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    log_stats(nginx_collection)
