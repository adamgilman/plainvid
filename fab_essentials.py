from fabric.api import env, local, run, cd, sudo
PIP_UPRGADED = False

def aptget(package):
	if type(package) is list:
		for p in package:
			aptget(p)
	else:
		sudo("apt-get -y install %s" % package)

def gem(package):
	if type(package) is list:
		for p in package:
			gem(p)
	else:
		sudo("gem -y install %s" % package)

def upgrade_pip():
	aptget('python-pip')
	pip("pip", upgrade=True)
	PIP_UPRGADED = True


def pip(package, upgrade=False):
	if not PIP_UPRGADED:
		upgrade_pip()

	if type(package) is list:
		for p in package:
			pip(p)
	else:
		if upgrade:
			sudo("pip install %s --upgrade" % package)
		else:
			sudo("pip install %s" % package)

