import matplotlib.pyplot as plt
import time

finalArrayPoints = []

# Fungsi untuk menampilkan garis
def DrawLine(p0, p1) :
    arr = []
    arr.append(p0)
    arr.append(p1)
    x = [point[0] for point in arr]
    y = [point[1] for point in arr]
    plt.plot(x, y, marker='o', linestyle='-', color="black")

# Fungsi untuk membuat titik tengah antar 2 titik
def MakeNewPoint(p0, p1) :
    x = 0.5*p0[0] + 0.5*p1[0]
    y = 0.5*p0[1] + 0.5*p1[1]
    return (x,y)

# Iterasi rekursif
def DrawBezierCurve(p0, p1, p2, iteration) :
    if (iteration > 0) :
        q0 = MakeNewPoint(p0, p1)
        q1 = MakeNewPoint(p1, p2)
        q = MakeNewPoint(q0, q1)
        iteration -= 1
        DrawBezierCurve(p0, q0, q, iteration) # Left branch
        finalArrayPoints.append(q)
        DrawBezierCurve(q, q1, p2, iteration) # Right branch
    # else :
    #     Do Nothing

# Initialization
def BezierMain(p0, p1, p2, iteration) :    
    # Memulai perhitungan waktu
    start_time = time.time()
    print(start_time)
    
    # Divide and Conquer
    finalArrayPoints.append(p0)
    DrawBezierCurve(p0, p1, p2, iteration)
    finalArrayPoints.append(p2)
    
    # Menampilkan kurva bezier
    DrawLine(p0, p1)
    DrawLine(p1, p2)
    for i in range (len(finalArrayPoints) - 1) :
        DrawLine(finalArrayPoints[i], finalArrayPoints[i + 1])
    
    # Menghentikan perhitungan waktu
    end_time = time.time()
    print(end_time)
    elapsed_time = end_time - start_time
    plt.gca().set_aspect('equal', adjustable='box')
    x_min, x_max = plt.xlim()
    y_min, y_max = plt.ylim()
    center_x = (x_min + x_max) / 2
    center_y = y_max
    plt.text(center_x, center_y, f"Elapsed time: {elapsed_time:.4f} seconds", fontsize=12, ha='center')
    
    plt.grid(True)
    plt.show()
    
    # Mau visualisasi?
    print("\nWanna see the visualization?")
    answer = int(input("No (0) / Yes (1): "))
    
    if (answer == 1) :
        for i in range (iteration) :
            # Hapus array 
            finalArrayPoints.clear()
        
            # Divide and Conquer
            finalArrayPoints.append(p0)
            DrawBezierCurve(p0, p1, p2, i+1)
            finalArrayPoints.append(p2)
            
            # Menampilkan kurva bezier
            DrawLine(p0, p1)
            DrawLine(p1, p2)
            for i in range (len(finalArrayPoints) - 1) :
                DrawLine(finalArrayPoints[i], finalArrayPoints[i + 1])
            plt.show()