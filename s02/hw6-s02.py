user1 = {
    "username":"admin",
    "pass": "12345"
}

while True:
    in1 = input(str("Hi! Please Type Your UserName: "))
    in2 = input(str("Type Your Password: "))

    if in1 == user1["username"] and in2 == user1["pass"]:
        print("Welcome Back ...")
        break

    elif in1 != user1["username"]:
        print("Username NOT FOUND <!>")
    elif in2 != user1["pass"]:
        print("Password Not Found <!>")
    
    