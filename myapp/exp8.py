import mysql.connector as mysql
import getpass, os


GET_USER_DATA_QUERY = 'SELECT username,password FROM auth WHERE username="{}"'
CHECK_USER_QUERY = 'SELECT username FROM auth WHERE username="{}"'
ADD_USER_QUERY = 'INSERT INTO auth VALUES ("{}","{}")'
CREATE_AUTH_TABLE = "CREATE TABLE auth (username VARCHAR(20), password VARCHAR(20))"


def connect_database():

   mysql_user = getpass.getpass("enter the username : ")
   mysql_password = getpass.getpass("enter the password : ", stream=None)
   global mydb
   mydb = mysql.connect(
       host="localhost",
       user=mysql_user,
       password=mysql_password,
       auth_plugin="caching_sha2_password",
       database="ostplexp8",
   )
   global cur
   cur = mydb.cursor(buffered=True)


def create_auth_table():
   try:
       cur.execute(CREATE_AUTH_TABLE)

   except Exception as error:
       print(error)


def check_user_data(username: str):
   """
   :params: username
   :return: True if user exists
            False if user does not exist
   """
   try:
       cur.execute(CHECK_USER_QUERY.format(username))
       if cur.fetchone() != None:
           return True
       return False
   except:
       return False


def add_user_data(username: str, password: str):
   """
   :params: username, password
   """
   try:
       if check_user_data(username):
           raise Exception("User already exists")
       cur.execute(ADD_USER_QUERY.format(username, password))
       mydb.commit()
       return True
   except Exception as error:
       print(error)
       mydb.rollback()
       return False


def get_user_data(username: str):
   """
   :params: username
   """
   try:
       if not check_user_data(username):
           raise Exception("User doesnt exists")
       cur.execute(GET_USER_DATA_QUERY.format(username))
       username, password = cur.fetchone()
       return username, password
   except Exception as error:
       print(error)
       return None, None


def check_valid_user_data(username: str, password: str):
   """
   :params: username, password
   """
   buffer_username, buffer_password = get_user_data(username)
   if buffer_username != username:
       print("Wrong username")
       return False
   if buffer_password != password:
       print("Wrong password")
       return False
   return True


# to create a password
def check_password():
   # if the user doesn't exist ask for the password
   password = input("Enter the password : ")
   # check if the length of the password is between 8 and 15 chars
   if not (len(password) >= 8 and len(password) <= 15):
       print("password should be of min 8 char and max 15 char. Please try again")
       check_password()
   # to check if the password contains atleast one small case char
   l_case = [i for i in password if i.islower()]
   if not l_case:
       print("password should contain atleast one lower case")
       check_password()
   # to check of the password contains atleast one upper case char
   u_case = [i for i in password if i.isupper()]
   if not u_case:
       print("password should contain atleast one upper case")
       check_password()
   # to check if the password containd atleast ont numeric case
   num_list = [str(i) for i in range(10)]
   n_case = [i for i in password if i in num_list]
   if not n_case:
       print("password should contain atleast one numeric value")
       check_password()
   else:
       return password


# to create a user
def create_user():
   username = input("Enter the username : ")
   # to check if the username already exists
   if check_user_data(username):
       print("username exists please try again")
       return
   password = check_password()
   if add_user_data(username, password):
       print("User added successfully!")


# for authentication
def check_user():
   # initialize tries as 0
   tries = 0
   while tries < 3:
       # take username and password form the user
       username = input("enter the username : ")
       password = input("enter the password : ")
       # check if uername exists
       if not check_user_data(username):
           print("User does not exist")
       if not check_valid_user_data(username, password):
           tries += 1
       if tries == 3:
           return False
       break
   print("User logged in successfully")
   return True


# main function
def main():
   connect_database()
   # create_auth_table()
   while True:
       menu = input("1. Create user\n2. Sign In\n: ")
       if menu == "1":
           create_user()
       elif menu == "2":
           check_user()
       else:
           break
   mydb.close()

if __name__ == "__main__":
   main()
