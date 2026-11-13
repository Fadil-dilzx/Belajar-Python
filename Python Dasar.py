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

# Encapsulation #
class BankAccount:
    def __init__(self, saldo_awal):
        self.__saldo = saldo_awal  # private attribute

    # getter
    def lihat_saldo(self):
        return self.__saldo

    # setter
    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
        else:
            print("Jumlah setor harus positif!")

    def tarik(self, jumlah):
        if 0 < jumlah <= self.__saldo:
            self.__saldo -= jumlah
        else:
            print("Saldo tidak cukup atau jumlah tidak valid!")

# Membuat objek
akun = BankAccount(1000)

# Mengakses saldo lewat method (bukan langsung)
print("Saldo awal:", akun.lihat_saldo())

akun.setor(500)
print("Setelah setor:", akun.lihat_saldo())

akun.tarik(300)
print("Setelah tarik:", akun.lihat_saldo())

# Inheritance #
# Parent class
class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def suara(self):
        print("Hewan ini memiliki suara.")

# Child class
class Kucing(Hewan):
    def suara(self):
        print(f"{self.nama} mengeong: Meow!")

class Anjing(Hewan):
    def suara(self):
        print(f"{self.nama} menggonggong: Guk guk!")

# Membuat objek dari class turunan
kucing = Kucing("Tom")
anjing = Anjing("Spike")

kucing.suara()
anjing.suara()

class Burung(Hewan):
    def suara(self):
        print(f"{self.nama} berkicau: Cuit cuit!")

    def terbang(self):
        print(f"{self.nama} sedang terbang!")
        
burung = Burung("Rio")
burung.suara()
burung.terbang()

class Mahasiswa:
    def __init__(self, nama, jurusan):
        self.nama = nama
        self.jurusan = jurusan

    def info(self):
        print(f"Nama: {self.nama}, Jurusan: {self.jurusan}")

class MahasiswaBaru(Mahasiswa):
    def __init__(self, nama, jurusan, tahun_masuk):
        super().__init__(nama, jurusan)   # memanggil constructor parent
        self.tahun_masuk = tahun_masuk

    def info(self):
        super().info()  # memanggil method parent
        print(f"Tahun Masuk: {self.tahun_masuk}")

maba = MahasiswaBaru("Andi", "Informatika", 2025)
maba.info()

# Polymorphism #
class Kucing:
    def suara(self):
        return "Meow"

class Anjing:
    def suara(self):
        return "Guk guk"

# Polymorphism in action
hewan = [Kucing(), Anjing()]

for h in hewan:
    print(h.suara())

class Hewan:
    def suara(self):
        return "Hewan bersuara"

class Kucing(Hewan):
    def suara(self):
        return "Meow"

class Anjing(Hewan):
    def suara(self):
        return "Guk guk"

# Semua objek diperlakukan sama sebagai 'Hewan'
daftar_hewan = [Kucing(), Anjing(), Hewan()]

for h in daftar_hewan:
    print(h.suara())
def cetak_suara(hewan):
    print(hewan.suara())

cetak_suara(Kucing())
cetak_suara(Anjing())

print(len("Python"))   # string
print(len([1, 2, 3]))  # list
print(len({"a": 1, "b": 2}))  # dictionary

# Abstraction #
from abc import ABC, abstractmethod

# Abstract class
class Hewan(ABC):
    @abstractmethod
    def suara(self):
        pass

# Subclass yang mengimplementasikan abstract method
class Kucing(Hewan):
    def suara(self):
        return "Meow"

class Anjing(Hewan):
    def suara(self):
        return "Guk guk"

# Tidak bisa langsung membuat object dari class abstract
# h = Hewan()  # Error!

# Hanya bisa dari subclass
k = Kucing()
a = Anjing()

print(k.suara())
print(a.suara())

from abc import ABC, abstractmethod

class Pembayaran(ABC):
    @abstractmethod
    def bayar(self, jumlah):
        pass

class Gopay(Pembayaran):
    def bayar(self, jumlah):
        print(f"Bayar {jumlah} menggunakan GoPay")

class Dana(Pembayaran):
    def bayar(self, jumlah):
        print(f"Bayar {jumlah} menggunakan Dana")

# Menggunakan abstraction
def proses_pembayaran(pembayaran, jumlah):
    pembayaran.bayar(jumlah)

# Memanggil dengan berbagai metode
proses_pembayaran(Gopay(), 50000)
proses_pembayaran(Dana(), 75000)
from abc import ABC, abstractmethod

class Pembayaran(ABC):
    @abstractmethod
    def bayar(self, jumlah):
        pass

class Gopay(Pembayaran):
    def bayar(self, jumlah):
        print(f"Bayar {jumlah} menggunakan GoPay")

class Dana(Pembayaran):
    def bayar(self, jumlah):
        print(f"Bayar {jumlah} menggunakan Dana")

# Menggunakan abstraction
def proses_pembayaran(pembayaran, jumlah):
    pembayaran.bayar(jumlah)

# Memanggil dengan berbagai metode
proses_pembayaran(Gopay(), 50000)
proses_pembayaran(Dana(), 75000)

# Exception Handling #
# Membagi angka dengan nol
#angka = 10
#hasil = angka / 0
#print("Hasil:", hasil)
#try:
 #   angka = 10
  #  hasil = angka / 0
   # print("Hasil:", hasil)
#except ZeroDivisionError:
 #   print("Error: Tidak bisa membagi dengan nol!")

try:
    data = int("abc")   
except ValueError:
    print("Error: Data tidak valid!")
except ZeroDivisionError:
    print("Error: Tidak boleh membagi dengan nol!")

try:
    angka = 10 / 2
except ZeroDivisionError:
    print("Error: Tidak bisa bagi nol!")
else:
    print("Perhitungan berhasil, hasil:", angka)
finally:
    print("Selesai memproses.")
def cek_umur(umur):
    if umur < 0:
        raise ValueError("Umur tidak boleh negatif!")
    else:
        print("Umur valid:", umur)

try:
    cek_umur(-5)
except ValueError as e:
    print("Error:", e)

# Handling (Read & Write file) #
# Membaca isi file
file = open("data.txt", "r")  
print(file.read())
file.close()

file = open("data.txt", "r")
for baris in file:
    print(baris.strip())  
file.close()

file = open("data.txt", "w")
file.write("Halo, ini data baru!\n")
file.write("Baris kedua...\n")
file.close()

file = open("data.txt", "a")
file.write("Baris tambahan...\n")
file.close()

with open("data.txt", "r") as file:
    isi = file.read()
    print(isi)

# Menulis file
with open("contoh.txt", "w") as file:
    file.write("Belajar Python itu menyenangkan!\n")

# Menambah data
with open("contoh.txt", "a") as file:
    file.write("Tambahan baris kedua.\n")

# Membaca file
with open("contoh.txt", "r") as file:
    for baris in file:
        print(baris.strip())
