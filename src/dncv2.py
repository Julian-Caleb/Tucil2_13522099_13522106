import matplotlib.pyplot as plt

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

# Iteration juga digunakan untuk warnanya
def DrawBezierCurve(arrOfPoints, iteration) :
    if iteration == 0 :
        return arrOfPoints
    else :
        newArrayOfPoints = []
        for i in range(len(arrOfPoints) - 1) :
            newArrayOfPoints.append(MakeNewPoint(arrOfPoints[i], arrOfPoints[i+1]))
        finalArrayOfPoints = [arrOfPoints[0]] + newArrayOfPoints + [arrOfPoints[-1]]
        newIteration = iteration - 1
        print(finalArrayOfPoints)
        
        for i in range(len(finalArrayOfPoints) - 1) :
            DrawLine(finalArrayOfPoints[i], finalArrayOfPoints[i+1])
        print("We do be drawin")
        plt.show()
        
        return DrawBezierCurve(finalArrayOfPoints, newIteration)
    
# Fungsi Pemrosesan
def BezierCurve(p0, p1, p2, iteration) :
    arr = [p0, p1, p2]

    DrawLine(p0, p1)
    DrawLine(p1, p2)
    plt.show()
    finalArr = DrawBezierCurve(arr, iteration)

    print("Final result")
    DrawLine(p0, p1)
    DrawLine(p1, p2)
    for i in range(len(finalArr) - 1) :
        DrawLine(finalArr[i], finalArr[i+1])
    plt.show()

