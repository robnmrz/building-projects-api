from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successfull(self):
        """ Test creating a new user with an email is successfull """
        email = "robinmerz@test.de"
        password = "testpassword"

        # creating a test user
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )
        
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Test the email for a new user is normalized """
        email = "robinmerz@TEST.COM"
        password = "testpassword"

        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """ Test creating user with no email rases error """
        password = "testpassword"
        
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email = None,
                password = password
            )

    def test_create_new_superuser_successfull(self):
        """ Test creating a new superuser is successfull """
        email = "robinmerz@test.de"
        password = "testpassword"
        
        user = get_user_model().objects.create_superuser(
            email = email,
            password = password
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)