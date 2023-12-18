from gempa import*

g1 = gempa("Banten 1.2", 1.2)
g2 = gempa("Palu 6.1", 6.1)
g3 = gempa("Cianjur 5.6", 5.6)
g4 = gempa("Jayapura 3.3", 3.3)
g5 = gempa("Garut 4.0", 4.0)

# Memanggil fungsi dampak untuk setiap objek
print(g1.dampak())
print(g2.dampak())
print(g3.dampak())
print(g4.dampak())
print(g5.dampak())