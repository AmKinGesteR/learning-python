# --------- While Loops --------- #

i = 1
while i < 6:    #dar hali ke i az 6 kpchok tar bod :
  print(i)    #print kon *i* ro az jomleye aval
  i += 1    #tedade jomle ye n + 1 , bad chap mishe (*CHON KE LOOP HAST)



i = 1
while i < 6:
  print(i)
  if i == 3:    #agar be 3 resid, motevaghet kon
    break
  i += 1



i = 0
while i < 6:
  i += 1
  if i == 3:
    continue    #agar be 3 resid, skip esh kon va nanevisesh, vali loop ro edame bede
  print(i)



i = 1
while i < 6:
  print(i)
  i += 1
else:    #*CHON KE BE 6 NEMIRESE (i < 6, agar <= bod, iradi nadasht), BIA ELSE O BEGO
  print("i is no longer less than 6")