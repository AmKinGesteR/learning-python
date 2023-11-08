sb1 = {
    "name": "-",
    "last-name": "-",
    "age": 00,
    "job": "Programmer",
    "height": 172,
    "games": ["Valorant", "CS2", "Minecraft"],
    "money": "none"
}

sb2 = {
    "name": "Cristiano",
    "last-name": "Ronaldo dos Santos Aveiro",
    "age": 38,
    "job": "Soccer Player",
    "height": 187,
    "games": ["none"],
    "money": "TOO MUCH"
}

print("My Dict= ", sb1)

sb1.update(sb2)
print("\n...... sb1.update(sb2) ......")
print("New Dict= ", sb1)