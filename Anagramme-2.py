#Datei öffnen
read_file = open('anagram.txt', 'r', encoding="utf-8")
#encoding = "utf-8" optional aber stellt sicher, weil das Betriebssystem auf Mac oft schon UTF-8 ist
#encoding = "ASCII" kennt nur a-z, A-Z, 0-9, keine Sonderzeichen
#encoding = "utf-8" kennt fast alles (Sonderzeichen, Emojis, usw.)

"""   
Variant 1:
wörter = f.readlines()
print(wörter)
= ['ampel\n', 'atlas\n', 'bier\n', 'brie\n', 'palme\n', 'teefisch\n', 'lampe\n', 'fernsehen\n', 'kamel\n', 'makel\n', 'karl\n', 'klar\n', 'nebel\n', 'leben\n', 'reifen\n', 'ferien\n', 'feiern\n', 'schaden\n', 'daschen\n', 'salat\n', 'rot\n', 'tor\n', 'ort\n', 'torte\n', 'toter\n', 'wein\n', 'liste\n', 'wien\n', 'angelsachsen\n', 'nachgelassen\n', 'augenzeugen\n', 'neuzugaenge\n', 'bierglas\n', 'bleisarg\n', 'stiel\n', 'bauernweisheit\n', 'treibhausweine\n', 'brautkleid\n', 'raubdelikt\n', 'dichterfuerst\n', 'schriftdeuter\n', 'dieselmotor\n', 'rostmelodie\n', 'liest\n', 'druckertests\n', 'durststrecke\n', 'langstrecke\n', 'steil\n', 'nacktsegler\n', 'schweinepest\n', 'wespenstiche\n', 'hochschule\n']
"""
#wir wollen '\n' aber nicht in die Liste, deswegen verwenden wir .strip() --> entfert LEERZEICHEN und ZEILENUMBRÜCHE am Anfang und Ende eines Strings

#Variant 2:
wörter = [line.strip() for line in read_file.readlines()]
print(wörter)

gruppen = {}        #Dictionary = {key: value}
for wort in wörter:
  schlüssel = ''.join(sorted(wort))

  if schlüssel not in gruppen:
    gruppen[schlüssel] = [wort,1]      #create a key and gives the value (in this case, value is a List)
  else:
    gruppen[schlüssel][1] += 1          #go into that key and grab index 1 of the List

#in neue Datei schreiben
write_file = open('anagram_output.txt', 'w', encoding="utf-8")
write_file.write("Wort;Anzahl\n")
for schlüssel, wert in gruppen.items():
  #gruppen.items() --> gibt alle key:value Paare als Liste von Tupeln
  erstes_wort = wert[0]
  anzahl = wert[1]
  write_file.write(f"{erstes_wort};{anzahl}\n")

#Dateien immer wieder schließen
read_file.close()
write_file.close()
#oder alternativ mit 'with', weil das schließt die Datei automatisch
#with open('anagram.txt', 'r', encoding="utf-8") as read_file:
#with open('anagram_output.txt', 'w', encoding="utf-8") as write_file:
