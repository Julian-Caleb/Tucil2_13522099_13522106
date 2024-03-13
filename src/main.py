import matplotlib.pyplot as plt
from divideandconquer import DrawBezierCurve, DrawLine

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

# Pemrosesan
# Gambar 2 garis dari 3 titik awal
DrawLine(p0, p1, 0)
DrawLine(p1, p2, 0)

# Iterasi
DrawBezierCurve(p0, p1, p2, iteration)
plt.grid(True)
plt.show()