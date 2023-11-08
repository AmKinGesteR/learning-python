# ye list darim, shamel chand ta esm, in chand ta esm ro mikhaym ke character e aval e har kodom ro ke hamashon to ye range hastan ro biare to ye list e jadid, va hamaro print begire.\


database = [
    ("Test1", "123"),
    ("Test2", "000")
]


print("Welcome. Please login.")

while True:
    username = input("Username: ")
    password = input("Password: ")

    if (username, password) in database:
        print(f"Welcome Back {username}")
        break

    elif username not in database:
        print("USERNAME NOT FOUND <!>")
    elif password not in database:
        print("PASSWORD NOT FOUND <!>")