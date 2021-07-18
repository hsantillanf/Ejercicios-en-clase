class logica:
    def __init__(self,lista=None):
        self.__lista=lista
    
    @property
    def lista(self):
        return self.__lista

    @lista.setter
    def lista(self,evalue):
        self.__lista=evalue
    

    def parImpar(self,numero):
        rec =numero%2
        if rec==0:
            print("{} es par". format(numero))
        else:
            print("{} es impar". format(numero))
    
    def perfecto(self,num):
        acu=0
        for contador in range(1,num):
            rec=num%contador
            if rec==0:
                acu=acu+contador
        if acu==num:
            print("{} es perfecto". format(num))
        else:
            print("{} no es perfecto". format(num))
    
        

class ejercicio(logica):
    def __init__(self,lista,numero):
        super().__init__(lista)
        self.dato=numero
    
    def sumar(self,n1,n2):
        return n1+n2
    
    def parImpar(self, numero):
        super().parimpar(numero)
        return numero%2

ejer =ejercicio([1,3,5],20)
ejer.perfecto(6)


if ejer.parImpar(6)==0:
    print(" es par")
else:
    print("es impar")
print(ejer.lista)
# ejer.parImpar()
#print(ejer.sumar(9,2))
    
