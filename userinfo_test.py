import unittest
from userinfo import Userinfo

class TestUser(unittest.TestCase):

   '''
   Test class that checks the behaviours of the Userinfo class.
   '''

   def setUp(self):
      
      self.new_userinfo = Userinfo("michael","password") # create user object


   def test_init(self):
      

      self.assertEqual(self.new_userinfo.username,"michael")
      self.assertEqual(self.new_userinfo.password,"password")

   def test_save_userinfo(self):

      self.new_userinfo.save_userinfo()
      self.assertEqual(len(Userinfo.userinfo_list),1)

   def tearDown(self):
      '''
      this will clean up after each test run.
      '''
      Userinfo.userinfo_list = []

   def test_save_multiple_userinfo(self):
      '''
      check if we can hold multiple user accounts
      '''
      self.new_userinfo.save_userinfo()
      test_userinfo = Userinfo("andrew","password") 
      test_userinfo.save_userinfo()
      self.assertEqual(len(Userinfo.userinfo_list),2)

   def test_delete_userinfo(self):
      '''
      test_delete_user to test if we can remove a user from our user list
      '''
      self.new_userinfo.save_userinfo()
      test_userinfo = Userinfo("michael", "password")
      test_userinfo.save_userinfo()

      self.new_userinfo.delete_userinfo()
      self.assertEqual(len(Userinfo.userinfo_list),1)


if __name__ == '__main__':
   unittest.main()
