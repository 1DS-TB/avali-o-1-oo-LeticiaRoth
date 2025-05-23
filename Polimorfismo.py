def emitir_som(animal):
    animal.falar()  #Recebe um objeto (animal), e chama o metodo falar

class Gato: #Classe recebe o metodo falar, porém responde diferente
    def falar(self):
        print("O gato mia")


class Cachorro: #Classe recebe o metodo falar, porém responde diferente
    def falar(self):
        print("O cachorro late")

animais = [Gato(), Cachorro()]

for animal in animais:
    emitir_som(animal)