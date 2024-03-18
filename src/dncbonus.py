import matplotlib.pyplot as plt
import time

# Inisialisasi global array
finalArrayPoints = []

# Fungsi untuk menampilkan garis antar 2 titik
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

# -- CONQUER -- 
# Fungsi untuk secara rekursif mencari titik tengah (1) antar 2 titik
# control point, kemudian mencari titik tengah (2) antar hasil 
# masing-masing titik tengah (1). Hal ini diulangi secara rekursif hingga
# berakhir dengan 1 titik tengah terakhir. 
# Kemudian, akan disatukan dari titik paling kiri masing-masing array input 
# rekursi, titik paling tengah, lanjut dengan titik paling kanan masing-masing
# array input rekursi. Untuk n titik, hasil akhirnya adalah (2n-1) titik
def PopulatePoints(controlPoints) :
    if (len(controlPoints) <= 1) :
        return controlPoints
    else :
        temp1 = []
        temp1.append(controlPoints[0])
        temp2 = []
        for i in range (len(controlPoints) - 1) :
            temp2.append(MakeNewPoint(controlPoints[i], controlPoints[i+1]))
        result = PopulatePoints(temp2)
        temp1.extend(result)
        temp1.append(controlPoints[-1])
        return temp1

# Algoritma utama secara divide and conquer
# Control points input akan dipopulate sesuai dengan fungsi PopulatePoints,
# di mana untuk n titik, dihasilkan 2n - 1 titik hasil.
# -- DIVIDE -- 
# Titik hasil kemudian akan diproses secara dipisah dan rekursif, dengan meng-
# gunakan titik tengah, yaitu pada index midArrIdx = (2n-1)//2, dan dibagi 
# pemanggilan fungsi dari idx 0 hingga midArrIdx dan idx midArrIdx hingga last 
# index. Divide dilakukan hingga iteration, yang setiap pemanggilannya -1, 
# mencapai nilai 0.
# -- CONQUER --
# Menggunakan finalArrayPoints sebagai array global (yang sebelumnya sudah diisi)
# titik paling pertama), akan ditambahkan dengan titik pada index midArrIdx setiap
# kali fungsi dipanggil. Setelah ditambahkan semua, finalArrayPoints nanti akan di-
# tambah dengan titik yang paling akhir
def DrawBezierCurve(controlPoints, iteration) :
    print("Iterasi mundur ke:", iteration)
    if (iteration > 0) :
        print("Sebelum populate: ", controlPoints)
        newControlPoints = PopulatePoints(controlPoints)
        print("Hasil populate:", newControlPoints)
        iteration -= 1
        midArrIdx = (len(newControlPoints)//2) # + 1 - 1 karena index
        print("Left branch:", newControlPoints[0:midArrIdx+1])
        print("Right branch:", newControlPoints[midArrIdx:])
        DrawBezierCurve(newControlPoints[0:midArrIdx+1], iteration) # Left branch
        finalArrayPoints.append(newControlPoints[midArrIdx])
        DrawBezierCurve(newControlPoints[midArrIdx:], iteration) # Right branch
    # else :
    #     Do Nothing
    
# Initialization
def BezierMain(controlPoints, iteration) :    
    # Print titik awal
    print("Control points awal:", controlPoints)
    
    # Memulai perhitungan waktu
    start_time = time.time()
    print(start_time)
    
    # Divide and Conquer
    finalArrayPoints.append(controlPoints[0])
    DrawBezierCurve(controlPoints, iteration)
    finalArrayPoints.append(controlPoints[-1])
    
    # Menampilkan kurva bezier
    for i in range (len(controlPoints) - 1) :
        DrawLine(controlPoints[i], controlPoints[i + 1])
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
            finalArrayPoints.append(controlPoints[0])
            DrawBezierCurve(controlPoints, i+1)
            finalArrayPoints.append(controlPoints[-1])
            
            # Menampilkan kurva bezier
            for j in range (len(controlPoints) - 1) :
                DrawLine(controlPoints[j], controlPoints[j + 1])
            for j in range (len(finalArrayPoints) - 1) :
                DrawLine(finalArrayPoints[j], finalArrayPoints[j + 1])
            plt.grid(True)
            plt.show()