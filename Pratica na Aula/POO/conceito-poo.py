#Classe base Animal
class Animal:
    def __init__(self, nome):
        self.nome = nome;
    
    def emitir_som(self):
        pass

    #Classe derivada: Cachorro (herda de Animal)
    class Cachorro(Animal):
        def emitir_som(self):
            return 'Au Au!';

    #Classe derivada: Gato (herda de Animal)
    class Gato(Animal):
        def emitir_som(self):
            return 'Meow!';

    #Classe derivada: Vaca (herda de Animal)
    class Vaca(Animal):
        def emitir_som(self):
            return 'Mouu!';

    #Função para emitir o som de um animal
    def emitir_som_animal(animal):
        print(animal.emitir_som());

    #Criando objetos das classes derivadas
    cachorro = Cachorro('Bety');
    gato = Gato('Jerry');
    vaca = Vaca('Luna');

    #Chamanda do método emitir som para cada objeto (animal)
    emitir_som_animal(cachorro);
    emitir_som_animal(gato);
    emitir_som_animal(vaca);