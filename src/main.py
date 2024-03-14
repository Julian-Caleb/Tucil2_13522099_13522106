import matplotlib.pyplot as plt
from dncv2 import BezierCurve

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
BezierCurve(p0, p1, p2, iteration)