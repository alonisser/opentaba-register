ssues for opentaba-register
create Models:
user:
extend user model:
	
* add many to many relationship between feeds and users
* add many to many relationship between sites and users
* add one to many relationship between subscription and users

app:
model (many to many to users) including domain (many), appsecret
add site model for different site

feed:

extend feed model:
* site relationship (one to one)

subscription: (glueing the specifc user and feed)
* many to one - to user
* many to one - to feed
* subscription removal hash

more tasks:
* registration form
* update wiki with roadmap
* celery task to run feed update - based on the management command
* new relic monitoring
* heroku deploy for prototype
* email   backend
* html email design

