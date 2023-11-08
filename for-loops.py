for name in ("Ahmad", "Ashkan"):
    print("SALAM " + name)


fruits0 = ["apple", "banana", "cherry"]
for x in fruits0:
  print(x)


for x in "banana":
  print(x)


fruits1 = ["apple", "banana", "cherry"]
for x in fruits1:
  print(x)
  if x == "banana":
    break


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

  