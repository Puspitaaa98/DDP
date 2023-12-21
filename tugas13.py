class animal:
    def __init__(self, nama, makanan, hidup, berkembang_biak,):
        self.n = nama
        self.m = makanan
        self.h = hidup
        self.b = berkembang_biak

class badak(animal):
    # Propertinya
    def __init__(self, nama, makanan, hidup, berkembang_biak,):
        self.n = nama
        self.m = makanan
        self.h = hidup
        self.b = berkembang_biak
    # Methodnya
    def cetak(self):
        print(f"Nama Hewan: {self.n}")
        print(f"Makanan: {self.m}")
        print(f"Hidup: {self.h}")
        print(f"Berkembang Biak: {self.b}")

class ikan(animal):
    # Propertinya
    def __init__(self, nama, makanan, hidup, berkembang_biak,):
        self.n = nama
        self.m = makanan
        self.h = hidup
        self.b = berkembang_biak
    # Methodnya
    def cetak(self):
        print(f"Nama Hewan: {self.n}")
        print(f"Makanan: {self.m}")
        print(f"Hidup: {self.h}")
        print(f"Berkembang Biak: {self.b}")

class ular(animal):
    # Propertinya
    def __init__(self, nama, makanan, hidup, berkembang_biak,):
        self.n = nama
        self.m = makanan
        self.h = hidup
        self.b = berkembang_biak
    # Methodnya
    def cetak(self):
        print(f"Nama Hewan: {self.n}")
        print(f"Makanan: {self.m}")
        print(f"Hidup: {self.h}")
        print(f"Berkembang Biak: {self.b}")



badak = badak("Badak Sumatra", "Rumput", "Darat", "Vivipar")
ikan = ikan("Gurami", "Pelet", "Air", "Herbivora")
ular = ular("Cobra", "Tikus", "Darat", "Vivipar")

print("\nInformasi Badak:")
badak.cetak()
print("_____________________________")
print("\nInformasi Ikan:")
ikan.cetak()
print("_____________________________")
print("\nInformasi Ular:")
ular.cetak()

