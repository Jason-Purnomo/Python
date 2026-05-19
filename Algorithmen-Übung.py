#Knoten definieren
Knote_A = {'element': 'A', 'printed': False, 'next': []}
Knote_B = {'element': 'B', 'printed': False, 'next': []}
Knote_C = {'element': 'C', 'printed': False, 'next': []}
Knote_D = {'element': 'D', 'printed': False, 'next': []}

#Transitionen zwischen den Knoten
Knote_A['next'] = [Knote_B]             #A -> B
Knote_B['next'] = [Knote_C, Knote_D]    #B -> C und B -> D
Knote_C['next'] = [Knote_B]             #C -> B
Knote_D['next'] = [Knote_A]             #D -> A

def printnodes(nodes, level=0):
  einrueckung = " " * 2*level
  print(einrueckung + nodes['element'] + "->")
  """
  Beispiel:
  Bei Level 0: "" + "A->"
  A->
  Bei Level 1: "  " + "B->"
      B->
  Bei Level 2: "      " + "C->"
          C->
  """
  if nodes['printed'] == True:
    return
    #ohne das würde die Funktion ewig laufen (B -> C -> B -> C -> ...)

    nodes['printed'] = True
  
  for node in nodes['next']:
    printnodes(node, level + 1)

printnodes(Knote_A)
