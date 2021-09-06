import unittest
from user_login import User


class TestUser(unittest.TestCase):
    """
    Test class to define test cases for the User class

    Args:
        unittest.TestCase: TestCase class creates test cases
    """

    def setUp(self):
        """
        Method run before each test to build a playground
        """
        self.new_user = User("Devin", "Belane", "Dbelane", "d@b.com", "belane")

    def test___init__(self):
        """
        test initialization to test object instantiation
        """
        self.assertEqual(self.new_user.first_name, "Devin")
        self.assertEqual(self.new_user.sur_name, "Belane")
        self.assertEqual(self.new_user.user_name, "Dbelane")
        self.assertEqual(self.new_user.email, "d@b.com")
        self.assertEqual(self.new_user.password, "belane")

    def tearDown(self):
        """
        method to clean up the user
        """
        User.user_list = []

    def test_save_user(self):
        """ """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

    def test_delete_user(self):
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list), 0)
