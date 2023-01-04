from random import randrange
def Imprime_mensagem_abertura():
    print("****************")
    print("***Bem Vindo ao jogo da forca!***")
    print("****************")

def carrega_palavra_secreta():
    #abrindo o arquivo
    """ arquivo = open("palavras.txt", "r")
    palavras = list()
    for linha in arquivo:
        palavras.append(linha.strip())
    arquivo.close() """ # fecha arquivos

    # outra forma de abrir arquivo 
    palavras = []
    with open("palavras.txt") as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip())
    # dessa forma acima o arquivo é fechado automaticamente

    numero = randrange(0,len(palavras)) # numero recebe conta de 0 ao numero de elemento da lista
    #print(palavras)
    #Strings são imutáveis, são sequências imutáveis!
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    lista=["_" for letra in palavra]
    return lista

def jogar():
    Imprime_mensagem_abertura()    
    palavra_secreta = carrega_palavra_secreta()

    #letras_acertadas = []
    # forma verbosa
    """ for letra in palavra_secreta: 
        letras_acertadas.append('_') """
    # forma sucinta
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(f'{letras_acertadas}')

    enforcou = False
    acertou = False
    erros = 0
    # enquanto n enforcou (true) e n acertou(true)
    while (not enforcou and not acertou):
        chute = pede_chute()
        print('Jogando...')
        #palavra_secreta.find(chute) #busca em qual posição a letra aparece primeiro (primeira ocorrÊNCIA)
        if(chute in palavra_secreta):
            marca_chute_correto(chute, palavra_secreta, letras_acertadas)                        
        else:
            erros+=1
            print(f'Você eroou. Restam {6-erros} tentativa(s).')
            desenha_forca(erros)
            
        enforcou = erros == 7
        acertou = '_' not in letras_acertadas
        print(f'{letras_acertadas}')
    
    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print(f"A palavra era {palavra_secreta}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def marca_chute_correto(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if (letra.upper() == chute.upper()):
            letras_acertadas[index] = letra
        index += 1
    print('Boa, acertou uma')

def pede_chute():
    chute = input('Qual letra? ').strip().upper()
    return chute

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):# se o nome do arquivo é o arquivo principal a ser executado
    jogar()

