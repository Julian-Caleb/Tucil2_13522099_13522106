import matplotlib.pyplot as plt
from divideandconquer import DrawBezierCurveDnC, DrawLine
from bruteforce import draw_bezier_curve_bf
import time

# Meminta input
print("-- INPUT TITIK --")
print("Minimal 2 titik")
n = int(input("Mau berapa titik: "))
while n < 2:
    print("Jumlah titik tidak valid")
    n = int(input("Mau berapa titik: "))
arrOfPoints = []
print("\n")

# Input titik
for i in range (n) :
    print(f"-- TITIK {i+1} --")
    x0 = float(input(f"Masukkan x{i+1} = "))
    y0 = float(input(f"Masukkan y{i+1} = "))
    arrOfPoints.append((x0, y0))
    print("\n")

# Input iterasi
print("-- ITERATION --")
print("Iterasi minimal sekali")
iteration = int(input("Mau berapa iterasi: "))
while iteration < 1:
    print("Jumlah iterasi tidak valid")
    iteration = int(input("Mau berapa iterasi: "))
print("\n")

print("-- PILIHAN ALGORITMA --")
print("1. Divide and Conquer\n2. Brute Force")
choice = int(input("Mau pake algoritma apa (1/2): "))
while (choice != 1) and (choice != 2):
    print("Pilihan algoritma tidak valid")
    choice = int(input("Mau pake algoritma apa (1/2): "))

start_time = time.time()

if choice == 1:
    # Pemrosesan
    # Menggambar garis awal (sebenarnya bisa dijadikan satu dengan penggambaran Bezier Curvenya, 
    # tapi akan dipisah untuk memudahkan pembacaan alur)
    for i in range (n-1) :
        DrawLine(arrOfPoints[i], arrOfPoints[i+1], 0)
    
    for i in range (n-2) :
        DrawBezierCurveDnC(arrOfPoints[i], arrOfPoints[i+1], arrOfPoints[i+2], iteration)
else:
    draw_bezier_curve_bf(arrOfPoints, iteration)

end_time = time.time()
elapsed_time = end_time - start_time
plt.gca().set_aspect('equal', adjustable='box')
x_min, x_max = plt.xlim()
y_min, y_max = plt.ylim()
center_x = (x_min + x_max) / 2
center_y = y_max
plt.text(center_x, center_y, f"Elapsed time: {elapsed_time:.4f} seconds", fontsize=12, ha='center')

plt.grid(True)
plt.show()