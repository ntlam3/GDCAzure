#!/usr/bin/python3
import sys
import logging
logging.basicConfig(stream=sys.stderr)
import os
print(os.listdir('/var/www/webapp/webapp'))
sys.path.insert(0,"/var/www/webapp/webapp")
#path='/var/www/webapp/webapp/'
#if path not in sys.path:
#	sys.path.insert(0,path)
#python_home='/usr/local/venvs/myvenv'
#activate_this ='/var/www/webapp/webapp/myvenv/bin/activate_this.py'
#execfile(activate_this, dict(__file__=activate_this))
	
from __init__ import app as application
application.secret_key = 'Add your secret key'
