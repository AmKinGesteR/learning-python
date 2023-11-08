# --------- if - else --------- #

#Equals: a == b
#Not Equals: a != b
#Less than: a < b
#Less than or equal to: a <= b
#Greater than: a > b
#Greater than or equal to: a >= b


if True:
    print('Hey?')     # Print 'Hey?'

if False:
    print('Eh?')     # Print nemide, Chon ke if FAGHAT TRUE ro mishnase


a = 20
b = 33

if a == b:
    print('print nemide')     # Print nemide, chon ke false hast

if a != b:
    print('doroste')     # Print *YAMATE*




# **** ELIF : agar if eshtebah bod, elif ro ejra kon
a2 = 33
b2 = 33
if b2 > a2:
    print("b is greater than a")
elif a2 == b2:
    print("a and b are equal")


# **** ELSE : baraxe if
a3 = 200
b3 = 33
if b3 > a3:
  print("b is greater than a")
else:
  print("a is greater than b")


# halat haye else o elif
a4 = 200
b4 = 33
if b4 > a4:
  print("b is greater than a")
elif a4 == b4:
  print("a and b are equal")
else:
  print("a is greater than b")


if b4 == a4:
  print("b is greater than a")
elif a4 > b4:
  print("a and b are equal")
else:
  print("a is greater than b")



# **** Short Hand If ... Else
print("A") if a > b else print("B")


# **** AND : HAMYE shart h BAYAD dorost bashan
a5 = 200
b5 = 33
c = 500
if a5 > b5 and c > a5:
  print("Both conditions are True")

# **** OR : Yeki az shart ham ham DOROST bashe okeye
if a5 > b5 or a5 > c:
  print("At least one of the conditions is True")

# **** NOT : bar axe if, masalan mige ke agar a > b NABOD
if not a > b:
  print("a is NOT greater than b")


# **** pass : migim ke garche in if dorost/ghalat hast, vali to azash begzar o velesh kon
if a <= b:
    pass