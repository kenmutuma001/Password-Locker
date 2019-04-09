from userinfo import Userinfo
from account import Account
import random
import getpass

def create_userinfo(username,password):
   '''
   Function to create new userinfo 
   '''
   new_userinfo = Userinfo(username,password)
   return new_userinfo

def create_account(username,accountFrom,acc_username,acc_password):

   '''
   Function to create new account
   '''
   new_account = Account(username,accountFrom,acc_username,acc_password)
   return new_account

def save_account(account):
   '''
   Saves created account
   '''

   Account.save_account(account)


def save_userinfo(userinfo):
   '''
   Saves userinfo
   '''
   Userinfo.save_userinfo(userinfo)

def disp_acc(name):
   '''
   Function to display saved account
   '''
   acc = Account.display_account()

   for account in acc:
      if account.username == name:
         return f'''
         ________________________________________
         {account.accountFrom.title()}  **  {account.acc_accountname}  **  {account.acc_password}
         ________________________________________ 
         '''


def find_acc(acc):
   '''
   Method to find specific account
   '''

   account = Account.find_account(acc)

   return f'''
              ******
   Your search for {acc} returned:
   _________________________________
   {account.accountFrom.title()}  |  {account.acc_accountname}  |  {account.acc_password}
   _________________________________
   '''


def del_acc(account):
   '''
   Method to delete account
   '''

   Account.delete_account(account)


def generate_password(length = 8):

   characters = ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','m','n','o','p','.','-','$','@']

   pass_word = ''

   while (len(pass_word) < length):
      index = random.randint(0,22)
      character = characters[index]
      pass_word += character

   return pass_word


# functions to reusable conditions

# main funtion that performs all the user actions

def app():

   while True:
      print('''
      


           Welcome To Password Locker    
      


      To LOG IN, enter 'l'. To SIGN UP, enter 's'. To exit, enter 'exit' .
      Note for new users you have to SIGN-UP first and then LOG IN
      ''')

      user_input = input()

      if user_input == 'l':
         print('''
             
         || LOG IN ||

             
         ''')
         print('Enter your username:')
         user_name = input()

         print('Enter Password:')
         pass_word = input()

         for userinfo in Userinfo.userinfo_list:
            if user_name == userinfo.username and pass_word == userinfo.password:
               print('''
                  ***
               Log in successful.
               ''')
               while True:
                  print('''
                  To ADD new account details, enter 'new'. To DELETE account details, enter 'del'. To FIND account details, enter 'find'. 
                  To LOG Out, enter 'out'.       
                  ''')

                  if disp_acc(user_name):
                     print(disp_acc(user_name))
                  else:
                     print('''

                                 ********
                     You don't have any saved account

                                 ********
                     ''')


                  userinfo_input = input()

                  if userinfo_input == 'new':
                     print("Enter account name (Twitter, Instagram,facebook, etc):")

                     acc_name = input().title()

                     print("Enter your chosen username:")

                     acc_user = input()

                     print("""
                     To enter your own password, enter 'm'.
                     To have us generate a password for you, press any key other than "m" then enter to have it generated for you.""")

                     action = input()

                     if action == 'm':
                        print("Enter a password. Ensure it's long enough")

                        pass_word = input('\n')

                        print(f"You've succesfully created new credentials. Here is your password: {pass_word}.")

                        save_account(create_account(user_name,acc_name,acc_user,pass_word))

                     else:
                        print("Please enter your desired password length. We advice greater than 8")

                        length = input()

                        if length == '':
                           length = 8
                                                   
                           pass_word = generate_password(int(length))
                           print(f"You've succesfully created new account details. Here's your password: {pass_word}")

                           save_account(create_account(user_name,acc_name,acc_user,pass_word))
                        else:
                           pass_word = generate_password(int(length))
                           print(f"You've succesfully created new account details. Here's your password: {pass_word}")

                           save_account(create_account(user_name,acc_name,acc_user,pass_word))


                  elif user_input == 'find':
                     print("Enter name of the account you want to find:")

                     acc_name = input('\n').title()
                     for account in Account.account_list:
                        if account.accountFrom == acc_name:
                           print(find_acc(acc_name))
                        else:
                           print('''
                                      !!!
                           There are no such credentials saved.''')
                        
                  elif user_input == 'del':
                     print('Enter name of account you want to delete:')

                     acc_name = input('\n').title()

                     for account in Account.account_list:
                        if account.accountFrom == acc_name:
                           del_acc(account)
                           print(f'''
                           You have successfully deleted the account details for {acc_name}.
                           ''')
                        else:
                           print(f'''
                           {acc_name} doesn't exist in your saved accounts.
                           ''')
                     
                  elif user_input == 'out':
                     break

            else:

               print("The username or password you entered isn't valid.")
               user_input = 's'

      elif user_input == 's':
         print('''
                 ****
        || Sign up for an account.||

         ______________________
         
                 ****

         After creating your account you'll be taken to the main page where you can log in using your sign up details.

         ----
         ''')

         print('Enter your username:')
         user_name = input()

         print('Enter Password:')
         pass_word = input()
         
         save_userinfo(create_userinfo(user_name,pass_word))

         print('''
             ***
         Sign up successful.
         ''')

      elif user_input == 'exit':
         exit()

   

print(app())
