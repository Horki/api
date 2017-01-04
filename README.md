# FLASK API
## Ubuntu 14.04, Python v3.4, NGINX v9.3, Redis, uWSGI, Postgre SQL

# Manual Run
- Install [Vagrant](https://www.vagrantup.com/docs/installation/)
- Install [Ansible](http://docs.ansible.com/ansible/intro_installation.html)
- Run `vagrant up`
- Connect to server `vagrant ssh`
- create `.env` file, see for all fields `.env.example`
- Init database `/vagrant$ python3 manage.py db upgrade` with migration
- Run seeder for dummy data `/vagrant$ python3 manage.py db seed`

# API services
- start service `sudo start api`
- restart service `sudo restart api`
- stop service `sudo stop api`

# Redis Queue Worker
- run *default* worker (TODO: add as service) `rq worker`

# NGINX services
- `sudo service nginx start`
- `sudo service nginx restart`
- `sudo service nginx reload`
- `sudo service nginx stop`

## Flask CLI commands
- `python3 manage.py db <command>` [Flask-Migration](https://flask-migrate.readthedocs.io/en/latest/)
- `python3 manage.py seed` run seeder to empty database
- `python3 manage.py test` run API tests

## API Docs
- http://127.0.0.1:8080/docs/
