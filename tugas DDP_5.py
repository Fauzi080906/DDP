#nomor 1
kendaraan = ['vario', 'motor', '250', 'biru', '2']
print(kendaraan)
kendaraan.append('15jt')
print(kendaraan)
kendaraan.append('beat')
print(kendaraan)
kendaraan.insert(2, 'scoopy')
print(kendaraan)

#nomor 2

import math

def hitung_luas():
    print("Pilih bangun datar untuk menghitung luasnya:")
    print("1. Persegi")
    print("2. Lingkaran")
    print("3. Segitiga")

    pilihan = int(input("Masukkan pilihan Anda (1/2/3): "))

    match pilihan:
        case 1:
            sisi = float(input("Masukkan panjang sisi persegi: "))
            luas = sisi ** 2
            print(f"Luas persegi adalah {luas} cm^2")
        case 2:
            jari_jari = float(input("Masukkan jari-jari lingkaran: "))
            luas = math.pi * (jari_jari ** 2)
            print(f"Luas lingkaran adalah {luas} cm^2")
        case 3:
            alas = float(input("Masukkan panjang alas segitiga: "))
            tinggi = float(input("Masukkan tinggi segitiga: "))
            luas = 0.5 * alas * tinggi
            print(f"Luas segitiga adalah {luas} cm^2")
        case _:
            print("Pilihan tidak valid, silakan pilih 1, 2, atau 3.")

hitung_luas()