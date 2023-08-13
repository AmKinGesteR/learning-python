# --------- moteghayerha --------- #

a = 1   # int
b = 2   # int
print(a + b)

c = 1.55     # float
d = 5.2549   # float
print(c + d)

e = 'mohammad'   # string (str)
f = 'hosein'    # string (str)
print(e + ' ' + f)



# --------- gereftane type e vorodi ha --------- #

print(type( 2 ))
print(type( 5.26 ))
print(type( 'asfasd' ))



# --------- rikhte gari = force kardane ye chizi ke eshtebahe, yani ini hast ke man migam --------- #

g = int ( 45.2 )  # in dar vaghe 'float' hast, vali man migam ke na, in 'int' hast
h = float ( 5 )   # in dar vaghe 'int' hast, vali man migam ke na, in 'float' hast
i = str ( '2' )   # harchi bezani tosh, behet string mide

print(type( g ))
print(type( h ))
print(type( i ))

print( g )   # vali chon ke goftam 'int' hast, ashar o hazf kard
print( h )   # vali chon ke goftam 'float' hast, ashar o ezafe kard
print( i )   # harchi bezani tosh, behet string mide



# --------- Strings --------- #

name = "Mohammad Hosein"
lastname = "Ebrahimi"
print(name + ' ' + lastname)


# j = "Mohammad Hosein" "Ebrahimi""
# print( j )    # Result : ERROR

print("#------------#")

k = "1 Name: Mohammad Hosein Ebrahimi \n Age: 17"   # Next Line "\n"
print( k )

print("#------------#")

l = "2 Name: Mohammad Hosein Ebrahimi \t Age: 17"   # 4 ta fasele "\t"
print( l )

print("#------------#")

m = "3 Name: Mohammad Hosein Ebrahimi \b Age: 17"   #BackSpace "\b"
print( m )

print("#------------#")

n = """4 Mohammad 
Hosein
Ebrahimi"""    #Next Line With """ jshs """
print( n )

print("#------------#")



# --------- Tajziye --------- #

o = "Mohammad"   #Hamon Dastane olaviat be tartib 0 , 1 , 2 , va ...
print( o[2] )    #Print "h"
print( o[0] )    #Print "M"
print( o[1:5] )  #Print az Harf e 1 ta 5 "oham" (Ta sare 5 ro chap kpn, Khode 5 ro chap nakon)
print( o[:5] )   #Print az aval ta sare 5
print( o[2:] )   #print az 2 ta akhar
print( o[-5:-1] )



# --------- strings + ints/floats --------- #

p = str(41646)
q = 'mohammad'
print( p + q )

p1 = 41646
q1 = 'mohammad'
print( str(p1) + q1 )


print("#------------#")


p2 = 17

q2 = "1 - My Age = " + str(p2)      #string + str(int/float)
print( q2 )



# --------- format --------- #

p3 = f"2 - My Age = {p2}"    #f'' = format , dige niazi nist + bezari, int/float ro to {} mizari, tabdil be string mishe. (hamon  ${} toye js)
print(p3)

name1 = 'Mohammad'
lastname1 = 'Ebrahimi'
print( f"Name: {name1} & LastName: {lastname1} & Age: {p2}" )

#q3 = f"Name: {name1} & LastName: {lastname1} & Age: {p2}"
#print( q3 )



# --------- bool = true or false --------- #

r = 10
r1 = 0
r2 = None
r3 = ''
r4 = ' '
r5 = {}
r6 = ()
r7 = []

print( bool(r) )    #Always TRUE (chon ke tosh yek chizi hast)
print( bool(r1) )   #Always False (chon ke tosh khalie va hichi nist)
print( bool(r2) )   #Always False (chon ke tosh khalie va hichi nist)
print( bool(r3) )   #Always False (chon ke tosh khalie va hichi nist)
print( bool(r4) )   #Always TRUE ( chon ke yek karakteri hast tosh [space ham karakter hesab mishe] )
print( bool(r5) )   #Always False (chon ke tosh khalie va hichi nist)
print( bool(r6) )   #Always False (chon ke tosh khalie va hichi nist)
print( bool(r7) )   #Always False (chon ke tosh khalie va hichi nist)



# --------- x --------- #