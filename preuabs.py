import csv  
from random import *

header = ["Name","Length","Crew","Passengers"]
nave2 = ['Halcón Milenario',randint(1, 1000) ,randint(1, 1000) ,randint(1, 1000) ]
nave3 = ['Ala-X ', randint(1, 1000), randint(1, 1000),randint(1, 1000),randint(1, 1000) ]
nave4 = ['Caza TIE ', randint(1, 1000), randint(1, 1000), randint(1, 1000)]
nave5 = ['Destructor Estelar',randint(1, 1000) , randint(1, 1000), randint(1, 1000)]
nave6 = ['Lanzadera imperial',randint(1, 1000) ,randint(1, 1000) , randint(1, 1000)]
nave7 = ['Nave Real Nubian 327 tipo J',randint(1, 1000) ,randint(1, 1000) , randint(1, 1000)]
nave8 = ['Nave de Control de Droides clase Lucrehulk', randint(1, 1000),randint(1, 1000) ,randint(1, 1000) ]
nave9 = ['Supremacy',randint(1, 1000) ,randint(1, 1000) ,randint(1, 1000) ]
nave10 = ['Speeders', randint(1, 1000), randint(1, 1000), randint(1, 1000)]


with open('naves.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
    writer.writerow(nave2)
    writer.writerow(nave3)
    writer.writerow(nave4)
    writer.writerow(nave5)
    writer.writerow(nave6)
    writer.writerow(nave7)
    writer.writerow(nave8)
    writer.writerow(nave9)
    writer.writerow(nave10)