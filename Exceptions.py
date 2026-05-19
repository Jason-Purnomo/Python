"""
Exceptions
3 wichtigste Begriffe =
try:        #Code der einen Fehler verursachen könnte
except:     #Was passiert wenn ein Fehler auftritt
raise:      #Einen Fehler absichtlich auslösen
"""

def add(x,y):
  return x + y
def sub(x,y):
  return x - y

#Eigene Exception definieren
class ProgramQuit (Exception):
  pass            # == kein extra Code nötig

try:
  while True:
    Eingabe = input("Eingabe [?, q, a, s]: ")

    if Eingabe == '?':
      print("HILFE TEXT")
    elif Eingabe == 'q':
      raise ProgramQuit       		#Exception absichtlich ausgelöst
    elif Eingabe == 'a':
      x = int(input("Wert 1: "))
      y = int(input("Wert 2: "))
      Ergebnis = add(x,y)
      print(Ergebnis)
    elif Eingabe == 's':
      x = int(input("Wert 1: "))
      y = int(input("Wert 2: "))
      Ergebnis = sub(x,y)
      print(f"Ergebnis: {Ergebnis}")

except ProgramQuit:
  print("Programm beendet sich...")

except ValueError:
  print("invalid")
