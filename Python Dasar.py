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
