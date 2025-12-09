temp = int(input("Saisir la température de l'eau: "))
temp_str = None

if temp <= 0:
    temp_str = "Solide"
elif temp < 100:
    temp_str = "Liquide"
else:
    temp_str = "Gazeux"

print(temp_str)