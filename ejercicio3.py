class sintaxis:
    instancia=0

    def _init_(self,dat="inicialización"):
        self.frase=dat

    def uvar(self):
      edad,peso=35,65.5
      nombre='Daniel Vera'
      sexo='M'
      civil=True
      print(nombre,edad,peso)
# tuplas inmutables
      usuario=()
      usuario=('Luna','4321','luna@gmail.com')

# listas mutables
      materias=[]
      materias=['Programación web', 'PHP', 'POO']
      materias[1]='Python'
      materias.append('GO')

# diccionario mutable
      docente={}
      docente={'nombre':'Daniel','edad':60,'fac':'Faci'}
      docente['nombre']='Ana'
      
      # print(usuario,materias,docente)
      print(usuario,usuario[0],usuario[0:1],usuario[-1])
      # print(materias,materias[2:],materias[:1],materias[::])
      #print(docente,docente['nombre'])
    


ej1= sintaxis()
ej1.uvar()
