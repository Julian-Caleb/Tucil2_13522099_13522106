import matplotlib.pyplot as plt
import numpy as np

# Inisialisasi array of random color
listColor = ["red", "lightblue", "green", "yellow", "orange", "purple"]

# Fungsi untuk menampilkan garis
def DrawLine(p0 : (float, float), p1 : (float, float), color : int) :
    arr = []
    arr.append(p0)
    arr.append(p1)
    x = [point[0] for point in arr]
    y = [point[1] for point in arr]
    plt.plot(x, y, marker='o', linestyle='-', color=listColor[color%(len(listColor))])

# Fungsi untuk membuat titik tengah antar 2 titik
def MakeNewPoint(p0 : (float, float), p1 : (float, float)) :
    x = 0.5*p0[0] + 0.5*p1[0]
    y = 0.5*p0[1] + 0.5*p1[1]
    return (x,y)

# Fungsi untuk membuat garis yang menghubungkan 2 titik tengah 3 garis
def MakeNewLine(p0 : (float, float), p1 : (float, float), p2 : (float, float), color : int) :
    q0 = MakeNewPoint(p0, p1)
    q1 = MakeNewPoint(p1, p2)
    
    DrawLine(q0, q1, color)
    return q0, q1

# Fungsi rekursif untuk membuat kurva bezier
# Iteration juga digunakan untuk warnanya
def DrawBezierCurveDnC(p0 : (float, float), p1 : (float, float), p2 : (float, float), iteration : int) :
    if (iteration > 0) :
        q0, q1 = MakeNewLine(p0, p1, p2, iteration)
        print(f"Iterasi {iteration}, titik q0 = {q0}")
        print(f"Iterasi {iteration}, titik q1 = {q1}")
        iteration -= 1
        DrawBezierCurveDnC(p0, q0, q1, iteration)
        DrawBezierCurveDnC(q0, q1, p2, iteration)
    # else :
    #     Do nothing
    
# Alur Divide and Conquer:
# p0, p1, p2
# q0, q1
# p0, q0, q1
# q0, q1, p2