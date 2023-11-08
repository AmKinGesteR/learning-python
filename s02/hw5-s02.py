user1 = {
    "username":"admin",
    "pass": "12345"
}

in1 = input(str("Hi! Please Type Your UserName: "))
in2 = input(str("Type Your Password: "))

if in1 == user1["username"] and in2 == user1["pass"]:
    print("Welcome Back ...")
else:
    print("Your Password Or UserName Not Correct <!> Try Again.")