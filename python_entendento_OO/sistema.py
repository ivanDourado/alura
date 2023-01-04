class Sistema:
    def __init__(self):
        self.txt = ''
    
    def le_entrada(self ):
        self.txt = input('Digite o texto:')
    
    def exibe_saida(self):
        print(self.txt)

sistema = Sistema()

sistema.le_entrada()
sistema.exibe_saida()