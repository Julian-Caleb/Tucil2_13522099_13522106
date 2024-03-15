import matplotlib.pyplot as plt
import math
from typing import List, Tuple

# Fungsi untuk mendapatkan koefisien berdasarkan segitiga Pascal (Pascal's Triangle)
def pt(i, j):
    return math.comb(i - 1, j - 1)

# Fungsi untuk menampilkan garis
def draw_line(p0 : (float, float), p1 : (float, float)) :
    arr = []
    arr.append(p0)
    arr.append(p1)
    x = [point[0] for point in arr]
    y = [point[1] for point in arr]
    plt.plot(x, y, marker = 'o', linestyle = '-', color = "red")

# Fungsi rekursif untuk membuat kurva bezier
# Iteration juga digunakan untuk warnanya
def draw_bezier_curve_bf(control_points: List[Tuple[float, float]], iteration: int) :
    arr_of_curve_points = []
    num_control_points = len(control_points)
    if (iteration > 0) :
        t = float(1 / iteration)
        for i in range (iteration + 1):
            x = 0.0
            y = 0.0
            for j in range(num_control_points):
                x += float(pt(num_control_points, j + 1) * ((1 - t * i) ** (num_control_points - 1 - j)) * ((t * i) ** j) * control_points[j][0])
                y += float(pt(num_control_points, j + 1) * ((1 - t * i) ** (num_control_points - 1 - j)) * ((t * i) ** j) * control_points[j][1])
            arr_of_curve_points.append((x, y))
        for k in range(iteration):
            draw_line(arr_of_curve_points[k], arr_of_curve_points[k + 1])