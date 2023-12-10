import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')

try:
    application = get_wsgi_application()
except Exception as e:
    print(f"Error during application startup: {e}")