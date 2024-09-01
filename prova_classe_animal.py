# Classe base Animal
class Animal:
    def falar(self):
        print("Este animal faz um som.")

# Subclasse Cachorro que herda de Animal
class Cachorro(Animal):
    def falar(self):
        print("O cachorro late.")

# Subclasse Gato que herda de Animal
class Gato(Animal):
    def falar(self):
        print("O gato mia.")

# Testando as classes
if __name__ == "__main__":
    # Criando instâncias das classes
    animal = Animal()
    cachorro = Cachorro()
    gato = Gato()

    # Chamando o método falar
    animal.falar()   # Saída: Este animal faz um som.
    cachorro.falar() # Saída: O cachorro late.
    gato.falar()     # Saída: O gato mia.
