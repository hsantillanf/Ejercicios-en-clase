from ejercicio10 import cargos

class empleados:
    secuencia=0
    def __init__(self,nomb,ced,suel,carg):
        # empleados.secuencia=empleados.secuencia
        # self.codigo=empleados.secuencia+1
        self.codigo=self.generarcodigo()
        self.nombre=nomb
        self.cedula=ced
        self.sueldo=suel
        self.cargo=carg
    def mostrar(self):
        print("codigo:{} nombre:{} cargo:{}-{}".format(self.codigo,self.nombre,self.cargo.codigo,self.cargo.descripcion))

    def generarcodigo(self):
        empleados.secuencia=empleados.secuencia+1
        return empleados.secuencia

cargo1=cargos("docente")
emp1=empleados("Daniel","0918455631",500,cargo1)
emp1.mostrar()
cargo2=cargos("Analista")
emp2=empleados("Ana","012162589",600,cargo2)
emp2.mostrar()
