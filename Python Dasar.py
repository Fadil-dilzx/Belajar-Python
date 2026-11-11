# Pengenalan Python #
print("Hello, Python!")
print("Hello dari Python!")

# Struktur Dasar Program Python #
if True:
    print("Kode ini berada di dalam blok if")
    print("Masih di dalam blok if")
print("Kode ini sudah di luar blok if")

nama = input("nama: ")
print("Halo,", nama)

def main():
    print("Hello dari fungsi main!")

if __name__ == "__main__":
    main()

# Tipe Data Dasar #
umur = 17
print(type(umur))  

tinggi = 170.5
print(type(tinggi))  

nama = "fadil"
print(type(nama))  

is_active = True
print(type(is_active))

buah = ["apel", "jeruk", "mangga"]
print(type(buah))  

warna = ("merah", "hijau", "biru")
print(type(warna))  

mahasiswa = {"nama": "Budi", "umur": 21, "jurusan": "Informatika"}
print(type(mahasiswa))  

angka = {1, 2, 3, 3, 4}
print(angka)  
print(type(angka))

x = 10       
y = float(x) 
z = str(x)   

print(y, type(y))  
print(z, type(z)) 

# Variable #
nama = "Andi"
umur = 25
tinggi = 170.5
is_active = True

print(nama)      
print(umur)      
print(tinggi)    
print(is_active) 

# Konstanta #
PI = 3.14159
GRAVITY = 9.8
MAX_RETRY = 5

print("Nilai PI:", PI)
print("Gravitasi:", GRAVITY)
print("Maksimum Percobaan:", MAX_RETRY)

TAX_RATE = 0.1  # 10% pajak

harga_barang = 50000
total = harga_barang + (harga_barang * TAX_RATE)

print("Total harga:", total)

# Operator Aritmatika #
x = 5
y = 10

print(x == y)  
print(x != y)  
print(x > y)   
print(x < y)   
print(x >= y)  
print(x <= y)  

a = True
b = False

print(a and b)  
print(a or b)   
print(not a)    

x = 10

x += 5
print(x)  

x -= 3
print(x)  

x *= 2
print(x)  

x /= 4
print(x)  

buah = ["apel", "jeruk", "mangga"]

print("apel" in buah)      
print("pisang" not in buah) 

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)     
print(a is c)     
print(a == c)     

# Control Flow #
nilai = 85

if nilai >= 90:
    print("A")
elif nilai >= 75:
    print("B")
else:
    print("C")

buah = ["apel", "jeruk", "mangga"]

for item in buah:
    print(item)

count = 0

while count < 5:
    print("Hitung:", count)
    count += 1

for i in range(1, 6):
    if i == 3:
        continue  
    if i == 5:
        break     
    print(i)

# Function #
def sapa():
    print("Halo, selamat datang di Python!")

sapa()

def sapa_nama(nama):
    print(f"Halo {nama}, semoga harimu menyenangkan!")

sapa_nama("Bang")
sapa_nama("Fadil")

def tambah(a, b):
    return a + b

hasil = tambah(5, 7)
print("Hasil penjumlahan:", hasil)

def sapa_orang(nama="Teman"):
    print(f"Halo {nama}!")

sapa_orang("Andi") 
sapa_orang()        

# *args
def jumlahkan(*angka):
    total = sum(angka)
    print("Total:", total)

jumlahkan(1, 2, 3, 4, 5)  



def biodata(**data):
    for key, value in data.items():
        print(f"{key}: {value}")

biodata(nama="Budi", umur=20, kota="Jakarta")

# List, Tuple, dan Set #
# Membuat list
buah = ["apel", "jeruk", "mangga"]

# Akses elemen
print(buah[0])   # apel

# Menambah elemen
buah.append("pisang")

# Mengubah elemen
buah[1] = "anggur"

# Menghapus elemen
buah.remove("mangga")

print(buah)

# Membuat tuple
warna = ("merah", "hijau", "biru")

# Akses elemen
print(warna[1])   # hijau

# Tuple tidak bisa diubah
# warna[0] = "kuning"  # Error

# Tapi bisa diakses dengan loop
for w in warna:
    print(w)

# Membuat set
angka = {1, 2, 3, 3, 4, 5}

print(angka)  # {1, 2, 3, 4, 5} (duplikat otomatis hilang)

# Menambah elemen
angka.add(6)

# Menghapus elemen
angka.remove(2)

# Operasi himpunan
ganjil = {1, 3, 5, 7}
genap = {2, 4, 6, 8}

print(ganjil | genap)   # Union
print(ganjil & genap)   # Intersection
print(ganjil - genap)   # Difference

# Dictionary #
# Membuat dictionary sederhana
mahasiswa = {
    "nama": "Budi",
    "umur": 20,
    "jurusan": "Informatika"
}

print(mahasiswa)

print(mahasiswa["nama"])    # Budi
print(mahasiswa.get("umur")) # 20

mahasiswa["angkatan"] = 2023   # Menambah data baru
mahasiswa["umur"] = 21         # Mengubah value umur

print(mahasiswa)

mahasiswa.pop("jurusan")   # Menghapus dengan key
del mahasiswa["nama"]      # Menghapus dengan del

print(mahasiswa)

for key, value in mahasiswa.items():
    print(key, ":", value)

kampus = {
    "mahasiswa1": {"nama": "Budi", "umur": 21},
    "mahasiswa2": {"nama": "Siti", "umur": 22}
}

print(kampus["mahasiswa1"]["nama"])  # Budi

#  Class & Object (OOP Dasar) #
# Membuat class
class Mahasiswa:
    def __init__(self, nama, jurusan):
        self.nama = nama
        self.jurusan = jurusan

    def sapa(self):
        print(f"Halo, nama saya {self.nama} dari jurusan {self.jurusan}")

# Membuat object dari class
mhs1 = Mahasiswa("Budi", "Informatika")
mhs2 = Mahasiswa("Siti", "Sistem Informasi")

# Memanggil method
mhs1.sapa()
mhs2.sapa()

class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def luas(self):
        return self.panjang * self.lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)

pp = PersegiPanjang(5, 3)
print("Luas:", pp.luas())
print("Keliling:", pp.keliling())

class BankAccount:
    def __init__(self, saldo):
        self.__saldo = saldo  # private attribute

    def lihat_saldo(self):
        return self.__saldo

    def setor(self, jumlah):
        self.__saldo += jumlah

akun = BankAccount(1000)
akun.setor(500)
print("Saldo:", akun.lihat_saldo())
