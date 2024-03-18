import matplotlib.pyplot as plt
import math
from typing import List, Tuple
import time

# Fungsi untuk menampilkan garis
def draw_line(p0 : (float, float), p1 : (float, float)):
    arr = []
    arr.append(p0)
    arr.append(p1)
    x = [point[0] for point in arr]
    y = [point[1] for point in arr]
    plt.plot(x, y, marker = 'o', linestyle = '-', color = "red")

# Fungsi rekursif untuk membuat kurva bezier
def draw_bezier_curve_bf(control_points: List[Tuple[float, float]], iteration: int):
    start_time = time.time()
    arr_of_curve_points = []
    num_control_points = len(control_points)
    if (iteration > 0) :
        t = float(1 / (iteration + 1))
        for i in range (iteration + 2):
            x = 0.0
            y = 0.0
            for j in range(num_control_points):
                x += float(math.comb(num_control_points - 1, j) * ((1 - t * i) ** (num_control_points - 1 - j)) * ((t * i) ** j) * control_points[j][0])
                y += float(math.comb(num_control_points - 1, j) * ((1 - t * i) ** (num_control_points - 1 - j)) * ((t * i) ** j) * control_points[j][1])
            arr_of_curve_points.append((x, y))
        for k in range(iteration):
            draw_line(arr_of_curve_points[k], arr_of_curve_points[k + 1])
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
