"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

# from dotenv import load_dotenv
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# project_folder = os.path.expanduser(BASE_DIR)  # adjust as appropriate
# load_dotenv(os.path.join(project_folder, '.env'))

application = get_wsgi_application()
