#!/usr/bin/env python3
"""Module that logs statistics about Nginx requests"""


def log_stats(mongo_collection):
    """Logs statistics about Nginx requests"""
    total_requests = mongo_collection.count()
    print(f"{total_requests} requests logged")

    get_requests = mongo_collection.count({"method": "GET"})
    print(f"{get_requests} GET requests")

    post_requests = mongo_collection.count({"method": "POST"})
    print(f"{post_requests} POST requests")

    put_requests = mongo_collection.count({"method": "PUT"})
    print(f"{put_requests} PUT requests")

    delete_requests = mongo_collection.count({"method": "DELETE"})
    print(f"{delete_requests} DELETE requests")
