# task2


Installation
------------

```shell sript
python3 -m venv venv
source venv/bin/activate
pip install whell
pip install -r requirements.txt
python manage.py makemigrations myapp
python manage.py migrate
python manage.py runserver
```


DataBackup
----------
```shell script
python manage.py dumpdata -e contenttypes  > myapp/fixtures/dumpdata.json
```
