import matematika

print(matematika.tambah(2, 3))   # Output: 5
print(matematika.kali(4, 5))     # Output: 20

import matematika as m

print(m.tambah(10, 5))
from matematika import tambah

print(tambah(7, 3))

import math

print(math.sqrt(16))  
print(math.pi)        

import operasi, geometri

print(operasi.kurang(10, 4))       
print(geometri.luas_persegi(5)) 

from operasi import kurang
from geometri import luas_persegi

print(kurang(20, 7))          
print(luas_persegi(8))        

import os
print(os.getcwd())  
import datetime
print(datetime.date.today())  
