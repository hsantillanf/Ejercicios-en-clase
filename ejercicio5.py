class ciclos:
    def __init__(self,numero1=5):
         self.numero=numero1
    
    def uwhile(self):
        # ciclo repetitivo
        
        car=input("Ingrese una vocal: ")
        car=car.lower()
        while car not in('a','e','i','o','u'):
            car=input("Ingrese vocal: ").lower()
        print("El caracter que ingresaste: {} es una vocal".format(car))

ciclos =ciclos()
ciclos.uwhile()
