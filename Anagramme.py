"""
wort = "bier"
fingerabdruck = ''.join(sorted(wort))
Variable heißt Fingerabdruck, der Begriff bedeutet zwei Wörter mit demselben sortierten string gehören zur selben Familie / sind Anagramme voneinander
sorted(wort) --> gibt eine Liste zurück --> ['b', 'e', 'i', 'r'] (Liste von kleinsten Buchstaben)
.join() --> klebt die Buchstaben wieder zu einem string zusammen ("beir")
"""

wörter = ["atlas", "otto", "bier", "brei", "salat", "brie"]
gruppen = {}        #Dictionary = {key: value}
for wort in wörter:
  schlüssel = ''.join(sorted(wort))


  if schlüssel not in gruppen:
    gruppen[schlüssel] = [wort,1]      #create a key and gives the value (in this case, value is a List)
  else:
    gruppen[schlüssel][1] += 1          #go into that key and grab index 1 of the List

print("Wort;Anzahl")
for schlüssel, wert in gruppen.items():
  #gruppen.items() --> gibt alle key:value Paare als Liste von Tupeln
  erstes_wort = wert[0]
  anzahl = wert[1]
  print(f"{erstes_wort};{anzahl}")
