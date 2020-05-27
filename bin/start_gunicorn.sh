#!/usr/bin/bash
source /home/www/code/learning-log/env/bin/activate
exec gunicorn -c "/home/www/code/learning-log/learning_log/gunicorn_conf.py" learning_log.wsgi
