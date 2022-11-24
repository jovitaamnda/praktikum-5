# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 22:19:45 2022

@author: jovita amanda putri
"""

n_huruf = []
n_angka = []
jum = 0

nilai_h = str(input("Masukkan Nilai : "))
nilai_a = float(input("Nilai : "))

n_huruf.append(nilai_h)
n_angka.append(nilai_a)

while nilai_h != "":
    nilai_h = str(input("Masukkan Nilai : "))
 
    if nilai_h != "":
     nilai_a = float(input("Nilai : "))
     n_huruf.append(nilai_h)
     n_angka.append(nilai_a)
     rata = sum(n_angka) / len(n_angka)
     print('rata - rata nilainya : ', rata)
