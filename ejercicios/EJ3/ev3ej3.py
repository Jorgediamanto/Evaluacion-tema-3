class Nave():

 

    def __init__(self, nombre, largo, tripulacion, numero_pasajeros):

        self.nombre = nombre

        self.largo = largo

        self.tripulacion = tripulacion

        self.numero_pasajeros = numero_pasajeros

    def ordenar_alfabeticamente(self,naves):
        c1 = []
        for x in naves:
            c1.append(x.nombre)
        
        c1.sort()
        print(c1)
    
            
            

    def ordenar_inverso_alfabeticamente(self,naves):
        c1 = []
        for x in naves:
            c1.append(x.nombre)
        
        c1.sort()
        c1.reverse()
        print(c1)
           

    def __str__(self):

        return "nombre: {}, largo: {}, tripulacion: {}, numero pasajeros: {}".format( self.nombre, self.largo, self.tripulacion, self.numero_pasajeros )

    def mayor_pasajeros(self,naves):
        c1 = []
        c3 = []
        c2 = []
        for x in naves:
            c1.append(x.numero_pasajeros)
            c3.append(x.nombre)
            c2.append(x.numero_pasajeros)

        c1.sort()
        c1.reverse()
        
        print(c1)
        print(c2)
        print(c3)
        contador = 0
        for x in c1:
            f=c2.index(x)
            print(c3[f])
            contador+=1
            if contador == 5:
                break

        """for z in range(5):
            y = max(c1)
            y1 = c4.index(y)
            #print(y1)

            c1.remove(y)
            #print(c1) 
            print(c3[y1])"""

        

    def mayor_tripulacion(self,naves):
        c1 = []
        c2 = []
        for x in naves:
            c1.append(x.tripulacion)
            c2.append(x.nombre)
        
        print(c1)
        print(c2)
        z = 0
        maxim=0
        for x in range(len(c1)):
            if maxim < c1[x]:
                maxim = c1[x]

        f = c2[c1.index(maxim)]
        print("Mayor cantidad de tripulantes: "+f)


    def empiezan_AT(self,naves):
        c1 = []
        c2 = []
        for x in naves:
            
            c2.append(x.nombre)
        print("Empieza por AT las naves: ")
        for x in c2:
            if x.startswith('AT'):
                print(x)


    def seis_o_mas(self,naves):
        c1 = []
        c2 = []
        for x in naves:
            c1.append(x.numero_pasajeros)
            c2.append(x.nombre)

        for x in c1:
                if x>=6:
                    print(c2[c1.index(x)])


    def mas_pequeña_mas_grande(self,naves):
        c1 = []
        c2 = []
        for x in naves:
            c1.append(x.largo)
            c2.append(x.nombre)


        print(c1)
        print(c2)
        print("eeeeo")
        minim = c1.index(min(c1))
        maxim = c1.index(max(c1))

        print(naves[minim])
        print(naves[maxim])

        



        



naves = []

a = Nave("Halcón Milenario", 150, 20, 100)
b = Nave("Estrella de la Muerte", 200, 15, 125)
d = Nave("ATpoori", 34, 1231, 120)
c = Nave("Xavineta", 4, 150, 1200)
e = Nave("Carromato", 100, 10, 132)
f = Nave("Dakota", 32, 330, 1322)

naves.append(a)
naves.append(b)
naves.append(c)
naves.append(d)
naves.append(e)
naves.append(f)

print(a)
print(b)


a.ordenar_alfabeticamente(naves)
a.ordenar_inverso_alfabeticamente(naves)
a.mayor_pasajeros(naves)
a.mayor_tripulacion(naves)
a.empiezan_AT(naves)
a.seis_o_mas(naves)
a.mas_pequeña_mas_grande(naves)


