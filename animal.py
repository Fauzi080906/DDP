##Buat class animal sebagai parent class. class animal mempunyai properti 4 properti (name, makanan, hidup, berkembang biak)

##buat minimal 3 class child (burung, ikan, ular, dll) setiap class child itu memiliki 2 properti dan method 

##buat minimal 2 objek untuk setiap class childnya. 

class Animal:
    def __init__(self, name, makanan, hidup, berkembang_biak):
        self.name = name
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak

    def info_animal(self):
        print('nama \t\t\t :', self.name,
              '\nmakanan \t\t :', self.makanan,
              '\nhidup \t\t\t :', self.hidup,
              '\nberkembang biak \t :', self.berkembang_biak)

binatang = Animal('kucing', 'daging/whiskas', 'darat', 'melahirkan')
binatang.info_animal()
print('--------------------------------------')