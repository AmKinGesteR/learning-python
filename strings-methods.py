# --------- strings methods --------- #

s = 'hello world'
s1 = 'Hello world'
s4 = 'HELLO WORLD'
print( s )
print( s.capitalize() )           # harfe aval bozorg mishe
print( s1.casefold() )            # harfe aval kochik mishe
print( s.count('l') )             # shemordane inke chand bar az in harf tekrar shode
print( s.find('w') )              # peyda kardane inke in harf, kojast?
     # --->  print( s.index('w') )    # hamon FIND hast

print( s.title() )                # avale kalame yaro bozorg mikone
print( s.upper() )                # hamaro bozorg mikone
print( s.lower() )                # hamaro kochik mikone

s2 = 'hello world {}'
print( s2.format('test') )        # miad jaye in {} to moteghayer, chizi ke to formate gozashtim mizare


s3 = '      hello world  WOW    '
print( s3.strip() )               # space haye aval va akhar e jomle ro delete mikone