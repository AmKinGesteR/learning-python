idk = {
  "brand": "Saipa",
  "model": "Pride",
  "color": "Kale Ghazi",
  "year": 1402
}


print(idk)
print(idk["model"])

x = idk["color"]
print(x)

print(len(idk))     #Shemordane Tedade Data Ha

x2 = dict(brand = "Saipa", model = "Pride", color = "Kale Ghazi", year = 1402)     #Tabdil Kardane *LIST* be *DICT*
print(x2)


del idk["color"]     #delete kardane yek data
print(idk)


idk.pop("brand")     #delete kardane yek data
print(idk)
     # idk.popitem()     #delete kardane AKHARIN ITEM


idk.clear()     #delete kardane data haye toye dict
print(idk)


#del idk     #Pak Kardane kole dict



myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)
print(myfamily["child2"])
print(myfamily["child2"]["name"])
