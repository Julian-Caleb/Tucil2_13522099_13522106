import matplotlib.pyplot as plt
from divideandconquer import DrawBezierCurve, DrawLine

# Meminta input
print("-- INPUT TITIK --")
print("Minimal 2 titik")
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
print("\n")

# Pemrosesan
# Menggambar garis awal (sebenarnya bisa dijadikan satu dengan penggambaran Bezier Curvenya, 
# tapi akan dipisah untuk memudahkan pembacaan alur)
for i in range (n-1) :
    DrawLine(arrOfPoints[i], arrOfPoints[i+1], 0)
    
for i in range (n-2) :
    DrawBezierCurve(arrOfPoints[i], arrOfPoints[i+1], arrOfPoints[i+2], iteration)

plt.grid(True)
plt.show()