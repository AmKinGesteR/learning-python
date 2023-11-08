# --------- Tuples --------- #
  ## Tuple ha mesle hamon *LIST* hastan, ba in tafavot ke nemishe taghireshon dad va *SARI TAR* az *LIST* hastan <!>

a = ('test1', 'g', 'test2', 'test3', 'g')
print(a)

print(type(a)) # gereftane type e in tuple


a2 = a.count('g') #shomaresh e yek harf ya data
print(a2)


tuple1 = ("abc", 34, True, 40, "male") #dar tuple mishe hame no data gozasht
print(tuple1)


#ezafe kardane yek item be tuple ba kalak rashti =))
b = [ a ]
b.append('test24143')
print(b)


c = (1, 4, 234, [434, 63465])
c[3][1] = 85
print(c)