import matplotlib.pyplot as plt
from dncbonus import BezierMain
from bruteforce import draw_bezier_curve_bf

# Meminta input jumlah titik
print("-- JUMLAH TITIK --")
n = int(input("Mau berapa titik: "))
print("\n")

# Meminta input titik
controlPoints = []
for i in range (n) :
    print(f"-- TITIK {i+1} --")
    x = float(input(f"Masukkan x{i+1}: "))
    y = float(input(f"Masukkan y{i+1}: "))
    controlPoints.append((x,y))
    print("\n")

# Meminta input banyak iterasi
print("-- ITERATION --")
iteration = int(input("Mau berapa kali iterasi: "))
print("\n")

# Memilih algoritma
print("-- PILIHAN ALGORITMA --")
print("1. Divide and Conquer\n2. Brute Force")
choice = int(input("Mau pake algoritma apa (1/2): "))
while (choice != 1) and (choice != 2):
    print("Pilihan algoritma tidak valid")
    choice = int(input("Mau pake algoritma apa (1/2): "))
print("\n")

# Eksekusi
if choice == 1:
    BezierMain(controlPoints, iteration)
else:
    draw_bezier_curve_bf(controlPoints, iteration)
