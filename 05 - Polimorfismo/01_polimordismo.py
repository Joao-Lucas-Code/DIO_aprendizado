class Passaro:
    def voar(self):
        print('Voando...')

class Pardal(Passaro):
    def voar(self):
        super().voar()

class Pinguim(Passaro):
    def voar(self):
        print("Avestruz não pode voar")

# FIXME: exemplo ruim do uso de herança para "Ganhar" o método voar
class Aviao(Passaro):
    def voar(self):
        print("Avião está decolando...")

def plano_voo(obj):
    obj.voar()


plano_voo(Pardal())
plano_voo(Pinguim())
plano_voo(Aviao())
    