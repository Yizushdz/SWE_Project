STARTUP:
mysql.server start;
python ./manage.py runserver;

SHUTDOWN:
mysql.server stop;
terminate web server CTRL+C
