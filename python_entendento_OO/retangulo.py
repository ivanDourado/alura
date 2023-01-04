class Retangulo:
    def __init__(self, x,y):
        self.__x = x
        self.__y=y
        self.__area = x*y
    
    def obter_area(self):
        return self.__area
    
r = Retangulo(7,6)
r.area= 7
print(r.obter_area())
""" 
Na linha em cima o objeto ganha um novo atributo com o nome area. Ou seja, temos um atributo __area 
E um novo com o nome area. No entanto, ao chamar r.obter_area(), continuamos acessar 
o atributo __area que foi inicializado com o produto de 7*6!
 """