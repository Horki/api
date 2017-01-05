# FLASK API
## Ubuntu 14.04, Python v3.4, NGINX v9.3, Redis, uWSGI, Postgre SQL

# Manual Run
- Install [Vagrant](https://www.vagrantup.com/docs/installation/)
- Install [Ansible](http://docs.ansible.com/ansible/intro_installation.html)
- Run `vagrant up`
- Connect to server `vagrant ssh`
- create `.env` file, see for all fields `.env.example`
- Init database `flask db upgrade` with migration
- Run seeder for dummy data `flask seed` *only first time*

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
- `flask db <command>` [Flask-Migration](https://flask-migrate.readthedocs.io/en/latest/)
- `flask seed` run seeder to empty database
- `flask test` run API tests *TODO: upgrade tests*

## Postman collection
- `/vagrant/postman/Flask API.postman_collection`

## Users
- all users have password *123456*
- list of all users http://127.0.0.1:8080/auth/all

## API Docs
- http://127.0.0.1:8080/docs/
