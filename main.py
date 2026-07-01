# Mini calculatrice en Python
def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Erreur: Division par zéro!"

print("=== Mini Calculatrice ===")
print("1. Addition")
print("2. Soustraction")
print("3. Multiplication")
print("4. Division")

choix = input("Choisis une opération (1-4): ")
x = float(input("Entrer le premier nombre: "))
y = float(input("Entrer le deuxième nombre: "))

if choix == "1":
    print("Résultat:", addition(x, y))
elif choix == "2":
    print("Résultat:", soustraction(x, y))
elif choix == "3":
    print("Résultat:", multiplication(x, y))
elif choix == "4":
    print("Résultat:", division(x, y))
else:
    print("Choix invalide!")
