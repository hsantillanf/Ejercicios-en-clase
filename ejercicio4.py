class condiciones:
    contador=0
    def _init_(self,numer1=0,numer2=0):
        self.numero1=numer1
        self.numero2=numer2
        numero= numer1+numer2
        self.numero3=numero

    def usoif(self):
        if self.numero1 == self.numero2:
            print('numero1{}, numero2:{}, son iguales'.format(self.numero1,self.numero2))
        elif self.numero1 == self.numero3:
            print('numer1{}, numero3:{}, son iguales'.format(self.numero1,self.numero3))
        else:
            print('Son diferentes')

con1= condiciones()
print(con1.numero1)
print(con1.numero2)

con2= condiciones(10,20)
print(con2.numero1)
print(con2.numero2)

cond3= condiciones(30,10)
cond3.usoif()
