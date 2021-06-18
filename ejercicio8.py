listaAlumnos= [{"nombre":"Luis","final":70},{"nombre":"Maria","final":60,"nombre":"Daniela","final":90}]
acu=0
cont=0
for alumnos in listaAlumnos:
    print(alumnos)
    for clave,valor in alumnos.items():
        print(clave,":",valor,end=" ")
        if clave=="final": acu=acu+valor
    cont +=1
print(acu/cont)        