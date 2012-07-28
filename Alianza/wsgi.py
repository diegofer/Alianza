import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Alianza.settings")

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)



#ESTA ES LA CONFIGURACION QUE TRAE WEBFACTION

# import os
# import sys

# from django.core.handlers.wsgi import WSGIHandler

# os.environ['DJANGO_SETTINGS_MODULE'] = 'Alianza.settings'
# application = WSGIHandler()

