
import os;

if os.getuid() == 0:
	print 'Please do not use root account'
	sys.exit(1)

cmd = 'wget -qO- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh'

result = os.system(cmd)

if result != 0:
	print 'Failed to download, please check your network settings'
	sys.exit(1)


