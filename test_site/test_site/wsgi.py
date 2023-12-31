"""
WSGI config for test_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import sys
sys.path.append('/home/ec2-user/test/test_site/')

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_site.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
