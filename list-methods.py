# --------- Lists --------- #

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")  # ezafe kardan be meghdar adadi ke dade
print(thislist) 



thislist2 = ["apple", "banana", "cherry"]
thislist2.append("orange")   # ezafe kardan be akhare list
print(thislist2)



thislist3 = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist3.extend(tropical)   # tarkib kardane 2 list
print(thislist3)



thislist4 = ["apple", "banana", "cherry"]
thislist4.remove("banana")   # remove kardan yek item
print(thislist4)
# >>> thislist5 = ["apple", "banana", "cherry", "banana", "kiwi"]
# >>> thislist5.remove("banana")          # faghat yek item remove mishe <!>
# >>> print(thislist5)



thislist6 = ["apple", "banana", "cherry"]
thislist6.pop(1)   # delete kardan ye item ba shomareye INDEX
print(thislist6)



thislist7 = ["apple", "banana", "cherry"]
del thislist7[2]   # delete kardane yek item ba shomareye INDEX
print(thislist7)



thislist8 = ["apple", "banana", "cherry"]
del thislist8   # delete kardane kole list -_-



thislist9 = ["apple", "banana", "cherry"]
thislist9.clear()   # item haye TOYE LIST delete mishe, list delete NEMISHE
print(thislist9)