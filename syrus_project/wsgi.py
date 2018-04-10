"""
WSGI config for syrus_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
import sys 

path1 = os.getcwd()
path2 = path1 + '/syrus_proyect'

from django.core.wsgi import get_wsgi_application

#sys.path.append('/var/www/syrus_project')
#sys.path.append('/var/www/syrus_project/syrus_project')

sys.path.append(path1)
sys.path.append(path2)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "syrus_project.settings")

application = get_wsgi_application()
