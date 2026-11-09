#Pengenalan Python#
print("Halo Python")

#Variabel dan Tipe Data#
# Menggunakan single quote
myFirstName = 'Fadila'

# Menggunakan double quote
myLastName = "Nurahman"

# Penulisan Angka sebagai string
myAge = "17"

# Penulisan string multiline
myHobby = """Hobi saya adalah bermain game.
"""

# Mencetak 2 variabel string dengan perintah print
print(myFirstName + " " + myLastName)
print("Umur saya " + myAge)

#variabel Boolean#
# Contoh penulisan boolean yang benar
a = True
b = False


print(a)

#Oprator pada Python#
#oprator aritmatika
a = 4
b = 2
# Penjumlahan
c = a + b
# Pengurangan
d = a - b
# Perkalian
e = a * b
# Pembagian
f = a / b
# Modulus
g = a % b
# Eksponensial
h = a ** b

# Cetak output
print(c) # 6
print(d) # 2
print(e) # 8
print(f) # 2
print(g) # 0
print(h) # 16
#Oprator camparison
a = 3
b = 5
# Perbandingan sama dengan
c = a == b
# Perbandingan tidak sama dengan
d = a != b
# Perbandingan lebih kecil
e = a < b
# Perbandingan lebih kecil sama dengan
f = a <= b
# Perbandingan lebih besar
g = a > b
# Perbandingan lebih besar sama dengan
h = a >= b

# Cetak output
print(c) # False
print(d) # True
print(e) # True
print(f) # True
print(g) # False
print(h) # False
#oprator logika
a = 3
b = 9

# Contoh Penggunaan "and"
print(a < 5 and b > 6) # True
print(a < 5 and b < 6) # False
print(a > 5 and b < 6) # False

# Contoh Penggunaan "or"
print(a < 5 or b > 6) # True
print(a < 5 or b < 6) # True
print(a > 5 or b < 6) # False

# Contoh Penggunaan "not"
print(not(a < 5 or b > 6)) # False
print(not(a > 5 or b < 6)) # True
