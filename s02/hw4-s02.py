# chadn ta dict shamele chand ta data, ba dastore if, agar yeki az in data ha bod, print kone ye chizi

sva1 = {
    "brand": "BMW",
    "model": "X1 crossover",
    "year": 2023,
}

sva2 = {
    "brand": "NISSAN",
    "model": "GT-R34 custom FH",
    "year": 2023,
}

sva3 = {
    "brand": "NISSAN",
    "model": "GT-R35",
    "year": 2023,
}



if sva1["brand"] == sva2["brand"]:
    print("Brand: BMW")
elif sva1["brand"] == sva3["brand"]:
    print("Brand: NISSAN GT-R")
else:
    print("Brand didn't Load...")

if sva2["brand"] == sva3["brand"]:
    print("Brand *NISSAN GTR* Loaded...")

if sva1["year"] == sva2["year"] == sva3["year"]:
    print("Year: 2023")
else:
    print("Can't Get Year...")