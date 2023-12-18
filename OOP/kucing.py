class kucing :
    nama = '..'
    warna = '..'
    umur = 0

    #constructor
    def __init__(self, nama, warna, umur):
        self.nama = nama
        self.warna = warna        
        self.umur = umur

    #methode untuk menampilkan data
    def data_kucing(self):
        print(f'nama kucing: {self.nama}')
        print(f'warna kucing: {self.warna}')
        print(f'umur kucing: {self.umur}')