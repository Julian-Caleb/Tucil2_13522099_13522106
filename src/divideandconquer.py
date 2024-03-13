import matplotlib.pyplot as plt
import numpy as np

# Fungsi untuk menampilkan garis
def DrawLine(p0 : (int, int), p1 : (int, int)) :
    arr = []
    arr.append(p0)
    arr.append(p1)
    x = [point[0] for point in arr]
    y = [point[1] for point in arr]
    plt.plot(x, y, marker='o', linestyle='-')

# Fungsi untuk membuat titik tengah antar 2 titik
def MakeNewPoint(p0 : (int, int), p1 : (int, int)) :
    x = 0.5*p0[0] + 0.5*p1[0]
    y = 0.5*p0[1] + 0.5*p1[1]
    return (x,y)

# Fungsi untuk membuat garis yang menghubungkan 2 titik tengah 3 garis
def MakeNewLine(p0 : (int, int), p1 : (int, int), p2 : (int, int)) :
    q0 = MakeNewPoint(p0, p1)
    q1 = MakeNewPoint(p1, p2)
    
    DrawLine(q0, q1)
    return q0, q1

def DrawBezierCurve(p0 : (int, int), p1 : (int, int), p2 : (int, int), iteration : int) :
    if (iteration > 0) :
        q0, q1 = MakeNewLine(p0, p1, p2)
        iteration -= 1
        DrawBezierCurve(p0, q0, q1, iteration)
        DrawBezierCurve(q0, q1, p2, iteration)
    # else :
    #     Do nothing
    
    
# p0, p1, p2
# q0, q1
# p0, q0, q1
# q0, q1, p2

# Meminta input
print("-- TITIK 1 --")
x0 = float(input("Masukkan x0 = "))
y0 = float(input("Masukkan y0 = "))
p0 = (x0, y0)
print("\n")

print("-- TITIK 2 --")
x1 = float(input("Masukkan x1 = "))
y1 = float(input("Masukkan y1 = "))
p1 = (x1, y1)
print("\n")

print("-- TITIK 3 --")
x2 = float(input("Masukkan x2 = "))
y2 = float(input("Masukkan y2 = "))
p2 = (x2, y2)
print("\n")

print("-- ITERASI --")
print("Iterasi dilakukan minimal sekali")
iteration = int(input("Mau iterasi berapa kali: "))

# Pemrosesan
# Gambar 2 garis dari 3 titik awal
DrawLine(p0, p1)
DrawLine(p1, p2)

# Iterasi
DrawBezierCurve(p0, p1, p2, iteration)

plt.show()