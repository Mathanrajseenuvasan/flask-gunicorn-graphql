import os
import multiprocessing

def number_of_workers():
    return (multiprocessing.cpu_count() * 2) + 1

bind = '127.0.0.1:5000'
worker_class = 'gevent'
worker_connections = '1000'
workers = 3
raw_env = [
    'DBHOST=localhost:3306',
    'DBUSER=root',
    'DBPASS=root',
    'DATABASE=posts',
]
# threads = 2
# debug = True
