import time

sva1 = {
    "brand": "BMW",
    "model": "X1 crossover",
    "year": 2023,
    "patch": "localhost:1224/as/cars/bmw/X1-crossover/p.lps",
    "3d-model": "localhost:1224/as/cars/bmw/X1-crossover/3d.3dps"
}

sva2 = {
    "brand": "GT-R",
    "model": "custom R34 FH",
    "year": 2023,
    "patch": "localhost:1224/as/cars/gt-r/custom-R34-FH/p.lps",
    "3d-model": "localhost:1224/as/cars/gt-r/custom-R34-FH/3d.3dps"
}

x = input(str("Select Models.... \n 1- BMW Model\n 2- GT-R Model\n"))
x2 = int(x)

if x == '1':
    print("Loading Patch....\n")
    time.sleep(2)
    print("Patch Loaded! =\n", sva1)


if x == '2':
    print("Loading Patch....\n")
    time.sleep(2)
    print("Patch Loaded! =\n", sva2)