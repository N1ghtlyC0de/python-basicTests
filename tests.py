import array
def decimaltoBin(n):
    binario = []
    if n >= 0:
        while n > 0:
            residuo = n % 2
            binario.append(residuo)      
            n = n // 2
    else:
        print(0)

    bin_numbers = [str(n) for n in binario]
    print("".join(bin_numbers[::-1]))

def tiketsCost(ages):
    cost = 0
    for age in ages:
        if age <= 2:
            cost += 0
        elif age > 2 and age < 13:
            cost += 14000
        elif age >= 13 and age <= 61:
            cost += 25000
        elif age >= 62:
            cost += 18000
    print(cost)
    
def yeartoAnimal(year):
    if year < 1:
        return "Año inválido"
    
    animals = ['Dragón', 'Serpiente', 'Caballo', 'Oveja', 'Mono', 'Gallo', 'Perro', 'Cerdo', 'Rata', 'Buey', 'Tigre', 'Liebre']
    print(animals[(year - 2000) % 12])

def isFibonacci(n):
    if n < 0:
        return False
    elif n == 0 or n == 1:
        return True
    else:
        a, b = 0, 1
        while b < n:
            a, b = b, a + b
        return b == n

def shapeType(n):        
    shapes = {
        3: 'triángulo',
        4: 'cuadrilátero',
        5: 'pentágono',
        6: 'hexágono',
        7: 'heptágono',
        8: 'octágono',
        9: 'eneágono',
        10: 'decágono'
    }

    if n < 3 or n > 10:
        return None
    
    else:
        return shapes[n]

def main():
    #decimaltoBin(int(input("Ingrese un numero decimal: "), 10))
    #tiketsCost([2,3,13])
    #yeartoAnimal(int(input("Ingrese un año: ")))
    print(isFibonacci(int(input("Ingrese un número: "))))
    #print(shapeType(int(input("Ingrese un número: "))))

if __name__ == "__main__":
    main()