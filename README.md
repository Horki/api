# FLASK API
## Ubuntu 14.04, Python v3.4, NGINX v9.3, Redis, uWSGI

# Run
1) Install [Vagrant](https://www.vagrantup.com/docs/installation/)
2) Install [Ansible](http://docs.ansible.com/ansible/intro_installation.html)
3) Run `vagrant up`

# Server
- `vagrant ssh`
- start service `sudo start api`
- restart service `sudo restart api`


## Endpoints 
- [GET] http://127.0.0.1:8080/data/test
- [GET] http://127.0.0.1:8080/data/cache