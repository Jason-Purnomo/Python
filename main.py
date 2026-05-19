# TI3 Praktikum 1 main
# MG
# 2025-03-03 15:20

"""Simulation einer Notenverteilung in einer Prüfung"""
import random
from aufgabe import *
def mkhisto(marks):
    return mkhisto_lsg(marks)
def print_histo(count):
    print_histo_lsg(count)



collect = []
for name,scala in MARKSCALES.items():
        d = as_dict(scala,20,10)
        lines = as_text(d).splitlines()
        collect.append(lines)


for line in zip(*collect):
    print(" | ".join(line))
print("\nLegende:", " | ".join(MARKSCALES.keys()))
print("-"*76)




n_studs=100 # Anzahl der Teilnehmenden an der Prüfung


tasks = [3,5,4,6,9,12,14,10,13,14] # "die Prüfung"

hi=sum(tasks) # volle Punktzahl, ohne Überhang
lo=int(hi*0.4) # 40% = bestanden
print("hi =",hi,", lo =",lo)
table_HM=as_dict(marks_HM, hi,lo)
assert table_HM is not None
print(as_text(table_HM))

# Abkürzung, leichter les- und wartbar im Code weiter unten
def calcmark(pt:str):
    return getmark(table_HM,pt)

# Leistungsfähigkeit der Teiln. zufällig verteilen
studs=[random.gauss(mu=0.7, sigma=0.3) for i in range(n_studs)]

# Prüfung schreiben
points=[]
for s in studs:
    pts = [s*t*random.uniform(0.5,1) for t in tasks]
    points.append(int(sum(pts)))

# ... und benoten
marks= [calcmark(str(p)) for p in points]
#print(marks)


# Historgramm erstellen
count = mkhisto(marks) # (selber überlegen oder Vorgabe nutzen)
#print(count)

# Historgramm ausgeben
print()
print("Notenhistogramm:")
print_histo(count) # (selber überlegen oder Vorgabe nutzen)
