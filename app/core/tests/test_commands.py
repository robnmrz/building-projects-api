from unittest.mock import patch # mocking
from django.core.management import call_command # calling commands in management folder (django convention)
from django.db.utils import OperationalError # operational error when data base isn't available on call
from django.test import TestCase

class CommandTests(TestCase):

    def test_wait_for_db_ready(self):
        """Test waiting for db when db is available"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi: # replacing standardfunction with mock object
            gi.return_value = True # returns 'True' everytime the database is called
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 1)

    @patch('time.sleep', return_value = True) # returns True, so the waiting time bewteen calls will be replaced an not wait --> speed up!
    def test_wait_for_db(self, ts):
        """Test waiting for db"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.side_effect = [OperationalError] * 5 + [True] # raises OperationalError first 5 times and returns true on sixth time
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 6)
