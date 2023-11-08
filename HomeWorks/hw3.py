name1 = '-'
lastname1 = '-'
age = 17
country1 = '-'
city1 = '-'
job1 = '              Programmer'
programs = [
    'Nodejs',
    'Html/Css',
    'C#',
    'JavaScript',
    'Shell',
    'Python'
]
games = [
    'cs go',
    'valorant',
    'MINECRAFT'
]

name = name1.upper()
lastname = lastname1.lower()
country = country1.find('ra')
city = city1.index('di')
job = job1.strip()
games1 = games[0].title()
games2 = games[1].capitalize()
games3 = games[2].casefold()


print(f' #-------------------------------------------------------------------------------------------------------#\n # Hello Man.                                                                                            #\n # My Name Is {name} {lastname}. Im {str(age)}. Im From {country} And {city}.                                          #\n # Im {job} And I know {programs[0]}, {programs[1]}, {programs[2]}, {programs[3]}, {programs[4]} And Now, Im Learning {programs[5]}.         #\n # Im Gamer And I Play {games1}, {games2}, {games3} And More...                                             #\n #-------------------------------------------------------------------------------------------------------#')
 