"""
WSGI config for proj project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
#from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

application = get_wsgi_application()

# ICI : On force WhiteNoise à servir le dossier de manière chirurgicale
#application = WhiteNoise(
#    application,
#    root='/home/jolegrand10/djproj/proj/staticfiles/',
#    prefix='/static/'
#)
