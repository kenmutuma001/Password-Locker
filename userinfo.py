class Userinfo:

   '''
   class generates the users info.That is the username and password.
   '''
   userinfo_list = []

   def save_userinfo(self):

      '''
      This method saves userinfo into the userinfo_list
      '''

      Userinfo.userinfo_list.append(self)

   def delete_userinfo(self):

      '''
      This will delete saved userinfo from userinfo_list
      '''

      Userinfo.userinfo_list.remove(self)

   @classmethod
   def find_userinfo(cls, string):
      '''
      this method accesses accounts in accounts_list
      '''

      for userinfo in cls.userinfo_list:
         if userinfo.username == string:
               return userinfo

   def __init__(self,username,password):

      '''
      Will define properties for this class
      '''

      self.username = username
      self.password = password


