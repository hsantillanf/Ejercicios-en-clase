class persona:
    siguiente=0
    def __init__(self,nombre="invitado",activo=True):
        #persona._siguiente= persona._siguiente+1
        self.__codigo=persona._siguiente()
        self.__nombre=self.__nombremayucula(nombre)
        self.activo=activo


    @property
    def nombre(self):
        return self.__nombre

    @property
    def nombre(self,nom):
        self.__nombre = nom


    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self,cod):
        self.__codigo = cod


    def siguiente(self):
        persona._siguiente=persona._siguiente+1
        return persona._siguiente


    def __nombremayucula(self,nomb):
        return nomb.upper()


    def mostrar_datos(self):
        return"codigo: {} nombre: {} activo: {}".format(self.codigo,self.nombre,self.activo)


class empleado (persona):
    
    def __init__(self,nombre="invitado",activo=True,sueldo=400):
        persona.__init__(self,nom,act)
        self.sueldo=sueldo
    
    def mostrar_datos(self):
        return persona.mostrar_datos(self)+" sueldo: "+str(self.sueldo)


per1=persona()
print(per1.nombre)
#print(per1.__nombreMayuscula("juan"))
per2= persona("daniel",False)
print(per2.nombre,per2.activo)

