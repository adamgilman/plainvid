import os, sys
from fabric.api import *
from fabric.decorators import *

from fab_essentials import aptget, pip#, gem

def vagrant():
    env.user = 'vagrant'
    env.hosts = ['127.0.0.1:2222']
    result = local('vagrant ssh-config | grep IdentityFile', capture=True)
    env.key_filename = result.split()[1]
    env.install_dir = "/vagrant/"
    env.activate = "source bin/activate"

    
def setup(rvm=True,ruby=True,rails=True):
	global HOME_DIR, SHELL_RC, RVM_DIR, RVM, GIT_RVM
	HOME_DIR="/home/%s" % env.user
	SHELL_RC=".zshrc"
	RVM_DIR=os.path.join(HOME_DIR,".rvm")
	RVM=os.path.join(RVM_DIR,"scripts/rvm")
	GIT_RVM = "git://github.com/wayneeseguin/rvm.git"

	if rvm:
	    install_rvm()
	if ruby:
	    install_ruby("head-ruby")
	    install_ruby("1.9.2")
	    default_ruby("1.9.2")
	if rails:
	    install_rails("1.9.2","3.1.0")


def install_rvm():
    with cd(HOME_DIR):
        run("mkdir -p ~/.rvm/src && cd ~/.rvm/src && rm -rf ./rvm/ && git clone git://github.com/wayneeseguin/rvm.git && cd rvm && ./install")
        run("echo 'if [[ -s %s ]] ; then source %s ; fi' >> %s"%(RVM_DIR,RVM, os.path.join(HOME_DIR,SHELL_RC)))

def install_ruby(version="head-ruby"):
    with cd(HOME_DIR):
        run("source %s && command rvm install %s"%(RVM,version))

def default_ruby(version="head-ruby"):
    with cd(HOME_DIR):
        run("source %s && rvm use %s --default"%(RVM,version))

def install_rails(ruby_version="1.9.2",rails_version="3.1.0"):
    with cd(HOME_DIR):
        run("source %s && rvm use %s && gem install rails -v '%s'"%(RVM,ruby_version,rails_version))

#@runs_parallel
def gem(package,ruby_version="1.9.2"):
    with cd(HOME_DIR):
        run("source %s && rvm use %s && gem install %s"%(RVM,ruby_version,package))


def build():
	aptget( ['build-essential', 'curl', 'byobu', 'autoconf', 'bison', 'git-core'] )
	
	setup(rails=False)
	gem('sinatra')
