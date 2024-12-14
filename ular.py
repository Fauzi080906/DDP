from animal import Animal

class Ular(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, kulit, berbisa):
        super().__init__( name, makanan, hidup, berkembang_biak),
        self.kulit = kulit
        self.berbisa = berbisa

    def info_ikan(self):
        super().info_animal(),
        print('kulit \t\t\t :', self.kulit,
              '\nberbisa \t\t :', self.berbisa)
        
ular_piton =Ular('piton', 'tikus/daging', 'darat', 'bertelur', 'licin bercorak', 
                 'tidak berbisa')
ular_piton.info_ikan()
print('---------------------------------------')
ular_laut = Ular('ular laut', 'daging/ikan kecil', 'laut', 'bertelur', 'licin dan berlendir', 
                 'sangat berbisa')
ular_laut.info_ikan()