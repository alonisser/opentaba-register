opentaba-register
=================

A server to handle email registrations for opentaba.info rss feeds
#Dependecies to pre install

python - 2.7.x
redis
celery
virtualenv (if you don't have that running yet)
install build dependencies for python-lxml. in ubuntu would be something like:

```sudo apt-get build-dep python-lxml```

#Install

```bash
#set everything in a virtualenv: assuming you are using the awesome virtualenv-wrapper
mkvirtualenv opentaba-register
workon opentaba-register
git clone https://github.com/alonisser/opentaba-register.git
cd opentaba-register
pip install -r requirements.txt #may need to do this twice
python manage.py syncdb
python manage.py migrate
bower install
```
test if everything working:

```python manage.py runserver```

and then checkout https://localhost:8000/ to see everthing works correctly
