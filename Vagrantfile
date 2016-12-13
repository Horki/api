# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

domain = "local.com"
settings = {
  :hostname => "myapp",
  :box => "ubuntu/trusty64",
  :ip => "192.168.33.10",
}

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
    # Box name
    config.vm.box = settings[:box]

    # Hostname
    # config.vm.host_name = "#{settings[:hostname]}.#{domain}"

    # Port forwarding
    config.vm.network :forwarded_port, guest: 80, host: 8080

    # Host-only access private network
    config.vm.network :private_network, ip: settings[:ip]

    config.vm.provision "ansible" do |ansible|
      ansible.playbook="ansible/playbook.yml"
      ansible.sudo=true
    end
end