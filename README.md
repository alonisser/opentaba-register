opentaba-register
=================

A server to handle email registrations for opentaba.info rss feeds
#Dependecies to pre install

python - 2.7.x
redis
celery
virtualenv (if you don't have that running yet)


#Install

```python
#set everything in a virtualenv.
git clone https://github.com/alonisser/opentaba-register.git
cd opentaba-register
virtualenv activate
pip install -r requirements.txt
python manage.py syncdb
python manage.py migrate
bower install
```
