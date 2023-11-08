import time
import sys
import getpass

database = [
    ("Test1", "123"),
    ("Test2", "000")
]


def main():
    print('YAMATE')

print("Welcome. Please login.")
while True:
    time.sleep(1)
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    time.sleep(1)
    if (username, password) in database:
        print("Welcome, " + username)
        main()
    else:
        print("User not found. Try again.")