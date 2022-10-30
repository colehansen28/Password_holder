# imports
import os.path


# welcome message
def welcome():
    print("welcome to Password holder")


# defining if file exists
def pathexistence():
    if os.path.exists("Password.txt"):
        pass
    else:
        file = open("Password.txt", 'w')
        file.close()


# adding new passwords to the file
def appendnew():
    while True:
        file = open("Password.txt", "a")
        print()

        username = input("Please enter the unsername: ")
        password = input("Please enter the password here: ")
        website = input("Please enter the website: ")

        print()

        usrnm = "UserName: " + username + "\n"
        pswrd = "Password: " + password + "\n"
        web = "Website: " + website + "\n"

        file.write("--------------------------\n")
        file.write(usrnm)
        file.write(pswrd)
        file.write(web)
        file.write("--------------------------\n")
        file.write("\n")
        file.close()
        x = input("Add another Password? (y/n)").lower()
        if x == str('n'):
            break


# reading the passwords in the file
def readpasswords():
    file = open('password.txt', 'r')
    content = file.read()
    file.close()
    print(content)


def Password_program():
    print('')
    welcome()
    print('')
    x = input("would you like to 'add' or 'read' a password?(a/r): ").lower()
    pathexistence()
    while True:
        if x == str('a'):
            appendnew()
            break
        elif x == str('r'):
            readpasswords()
            break
        else:
            print("(Error 200) Please type (a/r)")


# run the program
Password_program()
