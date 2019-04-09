import unittest
from account import Account

class TestCredentials(unittest.TestCase):

   '''
   Test class that checks the behaviours of the credentials class.
   '''

   def setUp(self):
      
      self.new_account = Account("michael","Instagram","michael", "password") # create contact object


   def test_init(self):
      
      self.assertEqual(self.new_account.username,"michael")
      self.assertEqual(self.new_account.accountFrom,"Instagram")
      self.assertEqual(self.new_account.acc_accountname,"michael")
      self.assertEqual(self.new_account.acc_password,"password")

   def test_save_account(self):

      self.new_account.save_account()
      self.assertEqual(len(Account.account_list),1)

   def tearDown(self):
      '''
      this will clean up after each test run.
      '''
      Account.account_list = []

   def test_save_multiple_accounts(self):
      '''
      check if a credentials account can hold multiple credentials
      '''
      self.new_account.save_account()
      test_account = Account("michael","Twitter","michael","password") 
      test_account.save_account()
      self.assertEqual(len(Account.account_list),2)


   def test_delete_account(self):
      '''
      test_delete_credentials to test if we can remove a credentials from our credentials list
      '''
      self.new_account.save_account()
      test_account = Account("michael","Instagram", "michael", "password")
      test_account.save_account()

      self.new_account.delete_account()
      self.assertEqual(len(Account.account_list),1)


if __name__ == '__main__':
   unittest.main()
