import os.path

base_path = os.path.split(os.path.abspath(__file__))[0]

import sys
sys.path.insert(0, base_path)

bind = '0.0.0.0:9655'
workers = 2
keepalive = 1
user = 'vp'
errorlog = os.path.join(base_path, 'log', 'error.log')
loglevel = 'warning'
proc_name = 'vp gunicorn'