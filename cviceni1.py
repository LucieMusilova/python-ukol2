sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

kod = input("Zadejte kód součástky: ")

if kod in sklad:
  mnozstvi = int(input("Zadejte kolik kusů součástky chcete koupit: "))
  if mnozstvi > sklad[kod]:
    print(f"Je nám líto, ale požadované množství produktu není na skladě. K dispozici je pouze {sklad[kod]} kusů součátky {kod}.")
    sklad.pop(kod)
  else:
    print(f"Požadované množství součástky {kod} je dostupné.")
    sklad[kod] -= mnozstvi
else:
  print("Součástka není skladem.")

print(sklad)