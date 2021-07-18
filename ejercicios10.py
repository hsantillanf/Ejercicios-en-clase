class cargos:
    secuenc=0
    def __init__(self,des="Sin cargo"):
        cargos.secuenc=cargos.secuenc+1
        self.codigo=cargos.secuenc
        self.descripcion=des

if __name__ == "__main__": 
    cargo1=cargos()
    # cargo1.codigo=1
    # cargo1.descrip="docente"
    print(cargo1.codigo,cargo1.descripcion)
    cargo2=cargos()
    # cargo2.codigo=2
    #cargo2.descripcion="director"
    print(cargo2.codigo,cargo2.descripcion)
    cargo3= cargos("analista")
    print(cargo3.codigo,cargo3.descripcion)
    # print(cargo.secuenc)
    # print(cargo1.secuenc)
    # print(cargo2.secuenc)
    # print(cargo3.secuenc)
