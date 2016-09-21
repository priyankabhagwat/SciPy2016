"""
WSGI config for online_test project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import sys


sys.path.insert(0, '/Site/scipy_in_2016/scipy/scipy2016')
sys.path.insert(1, '/Site/scipy_in_2016/scipy')
sys.path.insert(2, '/Site/scipy_in_2016/scipy_env/lib/python2.7/site-packages')
# We defer to a DJANGO_SETTINGS_MODULE already in the environment. This breaks
# if running multiple sites in the same mod_wsgi process. To fix this, use
# mod_wsgi daemon mode with each site in its own daemon process, or use

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scipy2016.settings")
activate_this = '/Site/scipy_in_2016/scipy_env/bin/activate_this.py'

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
