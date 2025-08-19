class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self._idade = idade # Privado

    def emitir_som(self):
        print(f"O {self.nome} fez um som")
    
    def get_idade(self):
        return self._idade
    
    def set_idade(self, nova_idade):
        if nova_idade >= 0:
            self._idade = nova_idade
        else:
            print("A idade não pode ser negativa.")


class Cachorro(Animal):
    def emitir_som(self):
        print(f"O cachorro {self.nome} late: Au au!")


class Gato(Animal):
    def emitir_som(self):
        print(f"O gato {self.nome} mia: Miau!")

c1 = Cachorro("Thor", 3)
g1 = Gato("Nuvem", 4)

c1.emitir_som()
g1.emitir_som()

print(f"A idade do {c1.nome} é: {c1.get_idade()}")
c1.set_idade(4)
print(f"A nova idade do {c1.nome} é: {c1.get_idade()}")
c1.set_idade(-1)