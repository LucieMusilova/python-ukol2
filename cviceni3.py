from staty import staty

zadany_region = input("Jaký region tě zajímá? ")
region_nalezen = False

for hodnoty in staty:
  if hodnoty["region"] == zadany_region:
    print(hodnoty["name"])
    region_nalezen = True

if not region_nalezen:
    print("Neznámý region.")