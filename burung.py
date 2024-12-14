
from animal import Animal

class Burung(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, paruh, warna_bulu):
        super().__init__( name, makanan, hidup, berkembang_biak),
        self.paruh = paruh
        self.warna_bulu = warna_bulu

    def info_burung(self):
        super().info_animal(),
        print('paruh \t\t\t :', self.paruh,
              '\nwarna bulu \t\t :', self.warna_bulu)
        
burung_beo =Burung('beo', 'biji-bijian','darat', 'bertelur', 'melengkung', 'warna-warni')
burung_beo.info_burung()
print('---------------------------------------')
burung_gagak = Burung('gagak', 'serangga', 'darat', 'bertelur', 'tajam', 'hitam')
burung_gagak.info_burung()