# FLASK API
## Ubuntu 14.04, Python v3.4, NGINX v9.3, Redis, uWSGI, Postgre SQL

# Run
1) Install [Vagrant](https://www.vagrantup.com/docs/installation/)
2) Install [Ansible](http://docs.ansible.com/ansible/intro_installation.html)
3) Run `vagrant up`
4) Connect to server `vagrant ssh`
5) create `.env` file, see for all fields `.env.template`
6) Init database `/vagrant$ python3 manage db upgrade` with migration
7) Run seeder for dummy data `/vagrant$ python3 manage db seed`

# API services
- start service `sudo start api`
- restart service `sudo restart api`
- stop service `sudo stop api`

# NGINX services
- `sudo service nginx start`
- `sudo service nginx restart`
- `sudo service nginx reload`
- `sudo service nginx stop`

## Flask CLI commands
- `python3 manage db <command>` [Flask-Migration](https://flask-migrate.readthedocs.io/en/latest/)
- `python3 manage seed` run seeder to empty database
- `python3 manage test` run API tests

## API Docs
- http://127.0.0.1:8080/docs/
