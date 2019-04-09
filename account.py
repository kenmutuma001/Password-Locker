class Account:

   '''
   Class that generates accountcredentials
   '''

   account_list = []

   def save_account(self):
      '''
      This method saves account in the account_list
      '''

      Account.account_list.append(self)

   def delete_account(self):
      '''
      This will delete saved account from account_list
      '''

      Account.account_list.remove(self)

   @classmethod
   def find_account(cls, string):
      '''
      this method accesses account in account_list
      '''

      for account in cls.account_list:
         if account.accountDetails == string:
               return account

   @classmethod
   def display_account(cls):
      '''
      method that returns the account details
      '''
      return cls.account_list

   def __init__(self, username, accountFrom, acc_accountname, acc_password):
      '''
      Will define properties for this class
      '''
      self.username = username
      self.accountFrom = accountFrom
      self.acc_accountname = acc_accountname
      self.acc_password = acc_password
