class Cliente:
    def __init__(self, nome):
        self.__nome = nome 

    # property para getter
    @property # o método abaixo acessará uma propriedade 
    def nome(self): # poderá acessar diretamentesem chamar método ()
        print("Chamando @property nome()")
        return self.__nome.title() # método title() deixa a 1º letra maiúscula

    #property para setter
    @nome.setter
    def nome(self, nome):
        print("Chamando setter nome()")
        self.__nome = nome