class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Iniciando a classe... ")
        self.nome=nome
        self.cor=cor
        self.acordados = acordado
    
    def __del__(self):
        print("Removendo a instancia da classe.")
    
    def latir(self):
        print("AuAu")

    def __str__(self):
        return f"Cachorro {self.nome} de cor {self.cor}"
    
c = Cachorro("Thor", "Beje")
print(c)
c.latir()