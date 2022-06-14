# The aim of the project is to create a computer based test using database

# Admin Module

# Importing regEX and mysql library
import re
import mysql.connector

# Calling our database
mycon = mysql.connector.connect(host='127.0.0.1', user='root', passwd='' , database='Project')
mycursor = mycon.cursor()


# Creating a class named ad
class ad():
    def __init__(self, me):
        self.me = me
        # ad.register()

# Declearing a function named register for admin members registration
    def register():
        print(" Register here to continue ")
# Using input to provide registration details
        name = input("  NAME>>")
        email = input("  EMAIL>>")
        password = input("  PASSWORD>>")
# Using reGEX to specify email format
        m = re.findall(r"[@gmail.com, @yahoo.com, @yahoo.ca, @ymail.com]$", email)
        if m:
            print("""               You're now registered
            You may proceed to login    """)
            # ad.login()
        else:
            print(" Invald email")
            ad.register()

# To insert details provided during registration into admin table in the database
        myquery = "INSERT INTO admin (Ful_Name, Email, Password) VALUES(%s, %s, %s)"
        value=(name,email,password)
        mycursor.execute(myquery, value)
        mycon.commit()
    
# Declearing a function named login for admin login 
    def login():
        print(" LOGIN PAGE")
# Admin is to input his/her login details
        email = input("EMAIL>> ")
        password = input("PASSWORD>> ")

# To select provided login details from database
        try:
            if email:
                query = "SELECT S_N, Ful_Name, Email FROM admin WHERE Email=%s AND Password=%s"
                val = (email, password)
                mycursor.execute(query, val)
                myreg = mycursor.fetchone()
                print(myreg)
                try:
                    if myreg[-1] == email:
                        ad.quest()
                except:
                    print('Login Error')
                    ad.login()
        except:
            print('Invalid login')
            ad.login()

# Declearing function named quest. This enables admin to input questions for cbt
    def quest():
        print(""" WELCOME ADMIN """)

        question = input('Enter question>> ')
        option_a = input('Enter option a>> ')
        option_b = input('Enter option b>> ')
        option_c = input('Enter option c>> ')
        answer = input("Enter the right anwer>> ")

# To insert the questions into database
        myquery = "INSERT INTO questions (Questions, Option_a, Option_b, Option_c, correct_answer) VALUES(%s, %s, %s, %s, %s)"
        val = (question, option_a, option_b, option_c, answer)
        mycursor.execute(myquery, val)
        mycursor.executemany((myquery, val),())
        mycon.commit()
        print(mycursor.rowcount, "records inserted successfully")
        ad.quest()

# ad.register()

