from fabric.api import env, local, run, cd, sudo

from fab_essentials import aptget, gem, pip

def vagrant():
    env.user = 'vagrant'
    env.hosts = ['127.0.0.1:2222']
    result = local('vagrant ssh-config | grep IdentityFile', capture=True)
    env.key_filename = result.split()[1]
    env.install_dir = "/vagrant/"
    env.activate = "source bin/activate"

def build():
	aptget( ['build-essential'] )