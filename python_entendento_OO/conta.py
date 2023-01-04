# definir receita / class
class Conta:
    def __init__(self, numero, titular, saldo, limite): # função construtora; 
        print(f'Construindo objeto . {self}{self}   ..') # self é a referênca q sabe onde encontrar o objeto q está sendo contruido em memória
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print(f'Saldo {self.saldo} do titular {self.titular}.')

    def deposita(self, valor):
        self.saldo += valor
    
    def saca(self, valor):
        self.saldo -= valor