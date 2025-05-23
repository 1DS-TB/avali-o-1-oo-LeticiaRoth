class Animal:
    def falar(self):
        print("Todo animal pode fazer algum som.")

class Gato(Animal): #Gato herda características do Animal
    def falar(self):
        print("O gato mia")


class Cachorro(Animal):
    def falar(self):
        print("O cachorro late")



a = Animal() #Crio o objeto da classem Animal
a.falar()    #Executo o metodo

g = Gato()
g.falar()

c = Cachorro()
c.falar()
