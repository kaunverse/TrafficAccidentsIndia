# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import mysql.connector as sqltor
import Table

f = open("Dtb_Prop.txt", "r")
r = f.read()
if r == "":
    f.close()
    print("Welcome to the Traffic Accidents dataset analysis! Everything is currently being set up for you.")
    print("(It is being assumed that you are an administrator or a technician.)")
    f = open("Dtb_Prop.txt", "w")
    host = input("Enter host name:\n")
    user = input("\nEnter user name:\n")
    passwd = input("\nEnter SQL password:\n")
    database = input("\nEnter database name:\n")
    f.write(host + '\n' + user + '\n' + passwd + '\n' + database)
    f.flush()
else:
    f.close()
    f = open("Dtb_Prop.txt", "r")
    host = f.readline()
    host = host[:-1]
    user = f.readline()
    user = user[:-1]
    passwd = f.readline()
    passwd = passwd[:-1]
    database = f.readline()
f.close()

mycon = sqltor.connect(host=host, user=user, passwd=passwd, database=database)
cursor = mycon.cursor()
Table.check()
print("MENU")
print()  # This is Satvik's part of the code
cont = 'Yes'
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
