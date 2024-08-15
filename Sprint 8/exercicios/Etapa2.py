animais = [
    "Leão", "Tigre", "Elefante", "Girafa", "Cachorro", 
    "Gato", "Cavalo", "Rinoceronte", "Zebra", "Macaco",
    "Panda", "Raposa", "Lobo", "Urso", "Baleia",
    "Golfinho", "Cobra", "Tartaruga", "Águia", "Pinguim"
]

animais.sort()

for animal in animais:
    print(animal)

with open("animais.csv", "w") as file:
    for animal in animais:
        file.write(animal + "\n")
