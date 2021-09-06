import unittest
from credentials import Credentials


class TestUser(unittest.TestCase):
    """
    Test class to define test cases for the User class

    Args:
        unittest.TestCase: TestCase class creates test cases
    """

    def setUp(self):
        """
        method to create test cases for the credentials class
        """
        self.new_credentials = Credentials("Twitter", "dbelane", "belane")

    def test___init__(self):
        """
        test to check object instantiation
        """
        self.assertEqual(self.new_credentials.site_name, "Twitter")
        self.assertEqual(self.new_credentials.user_name, "dbelane")
        self.assertEqual(self.new_credentials.password, "belane")

    def tearDown(self):
        """
        method to clean up after test case
        """
        Credentials.credentials_list = []
