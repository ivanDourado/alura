# definir receita / class
#encapsulamento:
# para tornar um atributo privado, deve-se preceder seu nome com 2 underscores __ ; exemplo __numero
class Conta:
    def __init__(self, numero, titular, saldo, limite): # função construtora; 
        print(f'Construindo objeto . {self}..') # self é a referênca q sabe onde encontrar o objeto q está sendo contruido em memória
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f'Saldo {self.__saldo} do titular {self.__titular}.')
    
    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def deposita(self, valor):
        self.__saldo += valor
    
    def saca(self, valor):
        if(valor<=(self.__saldo + self.__limite)):
            self.__saldo -= valor
        else:
            print(f'O valor {valor} passou o limite')
        
    @property
    def saldo(self):
        return self.__saldo
    @property
    def titular(self):
        return self.__titular
    @property
    def limite(self):
        return self.__limite
    @limite.setter
    def limite(self, limite):
        self.__limite = limite
""" 
conta = Conta(123, 'Ivan', 1000,2000)

conta2 = Conta(321,'Jai', 2000,4000)

conta.extrato()
conta2.extrato()

print(conta, conta2)

conta2.transfere(200 ,conta)

conta.extrato()
conta2.extrato()
conta.get_limite()
conta.get_saldo()
conta.get_titular() """


