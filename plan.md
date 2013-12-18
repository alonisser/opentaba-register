Issues for opentaba-register
extend user model:
	
* add many to many relationship between feeds and users
* add many to many relationship between sites and users
			
add app model (many to many to users) including domain (many), appsecret
add site model for different site

heroku deploy

extend feed model:
* unsubscribe link
* site relationship (one to one)
update wiki with roadmap
celery task to run feed update
new relic monitoring
