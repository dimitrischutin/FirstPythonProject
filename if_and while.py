age = int(input("Bitte gebe dein Alter ein: "))

if age < 18:
    print("Achtung der Nutzer ist jünger als 18!")
elif age == 18:
    print("Der Nutzer ist exakt 18 Jahre alt")
else:
    print("Der Nutzer ist volljährig")

print("---Programmende---")


counter = 5
while counter < 10:
    print("Der Code wird wiederholt")
    counter = counter + 1
