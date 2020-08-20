import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """Django command to pause exceution until database is available"""

    def handle(self, *args, **options): # args and options allow to include custom arguments and options
        self.stdout.write('Waiting for database...') # outputs string to the user, to tell whats going on
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)
        
        self.stdout.write(self.style.SUCCESS('Database available!')) # green output to indicate success