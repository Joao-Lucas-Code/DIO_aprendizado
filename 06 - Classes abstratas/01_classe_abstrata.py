from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV")
        print("TV LIGADA!")

    def desligar(self):
        print("Desligando a TV!")
        print("TV DESLIGADA")

controle = ControleTV()
controle.ligar()
controle.desligar()