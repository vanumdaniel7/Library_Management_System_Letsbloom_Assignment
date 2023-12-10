# your_app/apps.py

from django.apps import AppConfig
from django.db import connections
from django.db.utils import OperationalError
import logging

logger = logging.getLogger(__name__)

class YourAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'server'

    def ready(self):
        # Call the function at the start of your application
        try:
            # Try to establish a database connection
            with connections['default'].cursor():
                logger.info("Database connection successful")
        except OperationalError as e:
            logger.error("Database connection error.")
            logger.error("Exiting...")
            import sys
            sys.exit(1)

