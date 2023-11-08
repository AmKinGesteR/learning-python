me = {
  "name" : "-",
  "year" : 00
}
mom = {
  "name" : "-",
  "year" : 00
}
dad = {
  "name" : "-",
  "year" : 00
}

family = {
  "me" : me,
  "mom" : mom,
  "dad" : dad
}

a = family["me"]["name"]
b = family["mom"]["name"]
c = family["dad"]["name"]

print(f"My Name: {a}, My Mom Name: {b}, My Dad Name: {c}")