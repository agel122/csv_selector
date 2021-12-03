There are several rest api endpoints, implemented via django rest framework by following urls (via localhost):<br />
1) http://127.0.0.1:8000/api/start - POST with filename (data.csv as example):<br />
    will create record in database (SQLite as Django default) like:<br />
          {"id": 2, "filename": "data.csv", "dataresult": null, "status": "in_work"};<br />
    will start task via Celery+Redis to gather all data from required column of .csv file;<br />
    will update "dataresult" (data will be added) + will change "status" as soon, as task will be finished;<br />
2) http://127.0.0.1:8000/api/ongoing - GET will show "on-going" tasks like:<br />
          {"tasks in work": 0}<br />
3) http://127.0.0.1:8000/api/getresult?filename=data - GET will show record in database like:<br />
          {"id": 2, "filename": "data.csv", "dataresult": "89.2416354295115000", "status": "done"}<br />

All data-files are placed in FILES derectory (i didn't specify it via Django settings as static files directory).<br />

To start it you need:<br />
1) start Redis server in terminal like: <br />
redis-server<br />
and check it by:<br />
redis-cli ping<br />
(reply should be PONG)<br />
2) start django in venv terminal like:<br />
python manage.py runserver<br />
3) start celery worker in venv terminal like:<br />
celery -A datacheck worker -l INFO<br />

After, you can try url 1, check url 2 and try url 3 to be sure, that data has been uploaded finally via celery.<br />

p.s.<br />
I didn't hide Django secret key... yea, i know it...<br />
All of this looks...ugly. But...it works...seems like.<br />
