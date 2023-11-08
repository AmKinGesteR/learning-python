# --------- Sets --------- #
  # set hamon list  hast, vali ba in tafavot ke har bar item ha be tore randome jabeja mishan

soundboards = {'UwU', 'IQ', 'STFU', 'Namosan ?'}
soundboards2 = {'Nale kn koonkash', 'CUUUUUM', 'Namosan ?'}

print(soundboards)
print('UwU' in soundboards)   #Mibine Ke 'UwU' To List Hast Ya Na  (True/false)

soundboards.add('MOSHKEL DARI ?')   #Add kardan e Yek Item Be List
print(soundboards)

soundboards.update(soundboards2)   #Tarkib Kardane 2 Ta List
print(soundboards)

soundboards.union(soundboards2)   #Tarkib Kardane 2 Ta List
print(soundboards)

soundboards.remove('CUUUUUM')   #Remove Kardane Yek Item
print(soundboards)

soundboards.discard('STFU')   #Hamon Remove, **Vali Age Item Nabashe To list, Error Nemide**
print(soundboards)

x = soundboards.pop()
print(x)   #HarDafe Yeki Az Item Haro Mikeshe Biron
print(soundboards)   #List e Bedon On Item o Neshon Mide


soundboards.clear()   #Clear kardane Kole List
print(soundboards)

#del soundboards   #Delete Kardae Kole List
#print(soundboards)