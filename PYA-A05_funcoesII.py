def maior_numero(numero1, numero2, numero3):
    if numero1 >= numero2 and numero1 >= numero3:
        return numero1
    elif numero2 >= numero1 and numero2 >= numero3:
        return numero2
    else:
        return numero3
    
resultado = maior_numero(50, 180, 1530)
print("O maior número é:", resultado)
