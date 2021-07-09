 
"articulo, cliente,venta, ventadet"

class articulo:
    def __init__(self,cod,des,pre,sto):
        self.codigo=cod
        self.descripcion=des
        self.precio=pre
        self.stock=sto


class cliente:
    def __init__(self,ced,nom,dir,tel):
        self.cedula=ced
        self.numbre=nom
        self.direccion=dir
        self.telefono=tel


class venta:
    def __init__(self,fac,fe,cliente,detalle):
        self.factura=fac
        self.fecha=fe
        self.cliente=cliente
        self.detalle=detalle


class ventadet:
    def __init__(self,venta,articulo,precio,cantidad):
        self.articulo=articulo
        self.precio=precio
        self.cantidad=cantidad
        