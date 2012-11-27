# Some helpful utility commands.

all:
	heroku pgbackups:capture --expire
	git push heroku master
	heroku run python roda/manage.py syncdb --noinput  --settings=roda.settings.heroku
	heroku run python roda/manage.py migrate --settings=roda.settings.heroku
	heroku run python roda/manage.py collectstatic --noinput --settings=roda.settings.heroku

deploy:
	heroku pgbackups:capture --expire
	git push heroku master
	heroku run python roda/manage.py syncdb --noinput  --settings=roda.settings.heroku
	heroku run python roda/manage.py migrate --settings=roda.settings.heroku

style:
	git push heroku master
	heroku run python roda/manage.py collectstatic --noinput --settings=roda.settings.heroku

restoredata:
	heroku pgbackups:capture --expire
	curl -o latest.dump `heroku pgbackups:url`
	dropdb roda
	createdb roda
	pg_restore --verbose --clean --no-acl --no-owner -d roda latest.dump

createsite:
	heroku create --stack cedar
	heroku addons:add memcache:5mb
	heroku addons:add sendgrid:starter
	heroku addons:add heroku-postgresql:dev
	heroku addons:add pgbackups

shell:
	heroku run python roda/manage.py shell_plus --settings=roda.settings.heroku