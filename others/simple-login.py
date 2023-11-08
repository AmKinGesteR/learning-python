import time
from datetime import datetime
now1 = datetime.now()

# WELCOME MASSAGE
print("\033[92mHello Cutie! Welcome To That Data Base. Please Login To Your Account First...")

time.sleep(1)

# Loading User's Datas
ADMIN = {
    "type":"ADMIN",
    "username":"admin",
    "password":"admin",
    "created-date":"....."
}
user1 = {
    "type":"human",
    "username":"abc",
    "password":"12",
    "created-date":"....."
}
user2 = {
    "type":"human",
    "username":"def",
    "password":"1234",
    "created-date":"....."
}
user3 = {
    "type":"human",
    "username":"ghi",
    "password":"123456",
    "created-date":"....."
}


# LOGIN
x = input(str('\033[93mUserName? '))
y = input(str('\033[93mPassWord? '))


# ADMIN LOGIN
if x == ADMIN["username"] and y == ADMIN["password"]:
    z = input(str("\033[96mWELCOME ADMIN! Now, You Can Use This Commands ^^\n 1 > allusers\n 2 > date\n 3 > UPDATING .....\n >>> "))
    if z == "1":
        print(f"\033[95mALL USERS ^^\n\033[94muser1: {user1}\n\033[94muser2: {user2}\n\033[94muser3: {user3}")
    elif z == "2":
        print(f'\033[93mDate: {now1.strftime("%d/%m/%Y %H:%M:%S")}')


# USERS LOGIN
elif x == user1["username"] and y == user1["password"]:
    print('USER 1 LOADED')
elif x == user2["username"] and y == user2["password"]:
    print('USER 2 LOADED')
elif x == user3["username"] and y == user3["password"]:
    print('USER 3 LOADED')


else:
    print("\033[91mBRO, Your Pass or UserName Is Incorrect! Try Again...")