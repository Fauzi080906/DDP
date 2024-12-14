from animal import Animal

class Ikan(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, sirip, warna):
        super().__init__( name, makanan, hidup, berkembang_biak),
        self.sirip = sirip
        self.warna = warna

    def info_ikan(self):
        super().info_animal(),
        print('sirip \t\t\t :', self.sirip,
              '\nwarna \t\t\t :', self.warna)
        
ikan_hiu =Ikan('hiu', 'daging','laut', 'melahirkan', 'lancip', 'abu-abu')
ikan_hiu.info_ikan()
print('---------------------------------------')
ikan_paus_orca = Ikan('paus orca', 'daging', 'laut', 'bertelur', 'ekor(fluke)/horizontal', 'hitam')
ikan_paus_orca.info_ikan()