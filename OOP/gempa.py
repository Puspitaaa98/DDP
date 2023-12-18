class gempa:
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    def dampak(self):
        if self.skala < 2:
            return f"gempa di {self.lokasi} tidak terasa."
        elif 2 <= self.skala < 4:
            return f"gempa di {self.lokasi} menyebabkan bangunan retak-retak."
        elif 4 <= self.skala < 6:
            return f"gempa di {self.lokasi} menyebabkan bangunan roboh."
        elif self.skala >= 6:
            return f"gempa di {self.lokasi} menyebabkan bangunan roboh dan berpotensi tsunami."
        
    def call(self):
        print()