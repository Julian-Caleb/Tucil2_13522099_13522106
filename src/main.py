import matplotlib.pyplot as plt
from dncv2 import BezierCurve
from bruteforce import draw_bezier_curve_bf
import time

# Meminta input
print("-- TITIK 1 --")
x0 = float(input("Masukkan x0 = "))
y0 = float(input("Masukkan y0 = "))
p0 = (x0, y0)
print("\n")

print("-- TITIK P0 --")
x1 = float(input("Masukkan x1 = "))
y1 = float(input("Masukkan y1 = "))
p1 = (x1, y1)
print("\n")

print("-- TITIK P1 --")
x2 = float(input("Masukkan x2 = "))
y2 = float(input("Masukkan y2 = "))
p2 = (x2, y2)
print("\n")

print("-- ITERASI P2 --")
print("Iterasi dilakukan minimal sekali")
iteration = int(input("Mau iterasi berapa kali: "))
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
    BezierCurve(p0, p1, p2, iteration)
else:
    control_points = []
    control_points.append(p0)
    control_points.append(p1)
    control_points.append(p2)
    draw_bezier_curve_bf(control_points, iteration)

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