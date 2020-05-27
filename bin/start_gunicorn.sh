#!/usr/bin/bash
source /home/www/code/learning-log/ll_env/bin/activate
exec gunicorn -c "/home/www/code/learning-log/learning-log/gunicorn_conf.py" config.wsgi
