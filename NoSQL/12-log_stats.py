#!/usr/bin/env python3
"""
12-log_stats.py

يعرض إحصائيات عن سجلات Nginx المخزنة في MongoDB.
- Database: logs
- Collection: nginx
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    # السطر الأول: العدد الكلي للمستندات
    total_logs = nginx_collection.count_documents({})
    print("{} logs".format(total_logs))

    # السطر الثاني وما بعده: عدد المستندات لكل method
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    # السطر الأخير: عدد الطلبات GET على المسار /status
    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print("{} status check".format(status_check))
    