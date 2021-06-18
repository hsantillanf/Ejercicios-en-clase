listaNotas= [(30,40),[20,40,20],(50,40,20,10,5)]
acu=0
long=0
for notas in listaNotas:
    parcial=0
    print(notas,end=" ")
    for nota in notas:
        print(nota)
        long= long+1
        acu=acu+nota
        parcial += nota
    promparcial=parcial/len(notas)
    print("Notas parciales={} Promedio parcial={}".format(parcial,promparcial))
prom=acu/long
print("Total notas= {} - #notas={}: Promedio={} ".format(acu,long,prom ))
