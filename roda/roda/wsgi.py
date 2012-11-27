"""
WSGI config for roda project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""
import os

from django.core.wsgi import get_wsgi_application

#from barrel import cooper

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "roda.settings")

application = get_wsgi_application()
"""
REALM = "PRIVATE"
USERS = [('spam', 'eggs')]
application = cooper.basicauth(users=USERS, realm=REALM)(get_wsgi_application())
"""