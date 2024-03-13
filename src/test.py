import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def draw_bezier_curve_animation(control_points, num_frames=100):
    """
    Animate Bezier curve using divide and conquer approach.

    Parameters:
        control_points (list): List of control points [(x1, y1), (x2, y2), ...].
        num_frames (int): Number of frames for the animation.

    Returns:
        None
    """
    fig, ax = plt.subplots()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    line, = ax.plot([], [], color='b', lw=2)
    control_line, = ax.plot([], [], 'ro--', lw=1)

    def init():
        line.set_data([], [])
        control_line.set_data([], [])
        return line, control_line,

    def animate(frame):
        t = frame / (num_frames - 1)
        curve_points = de_casteljau(control_points, t)
        x = [point[0] for point in curve_points]
        y = [point[1] for point in curve_points]
        line.set_data(x, y)
        control_x = [point[0] for point in control_points]
        control_y = [point[1] for point in control_points]
        control_line.set_data(control_x, control_y)
        return line, control_line,

    def de_casteljau(points, t):
        if len(points) == 1:
            return points[0]
        new_points = []
        for i in range(len(points) - 1):
            x = (1 - t) * points[i][0] + t * points[i + 1][0]
            y = (1 - t) * points[i][1] + t * points[i + 1][1]
            new_points.append((x, y))
        return de_casteljau(new_points, t)

    ani = animation.FuncAnimation(fig, animate, frames=num_frames, init_func=init,
                                  interval=50, blit=True, repeat=False)
    plt.title('Bezier Curve Animation')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)
    plt.show()

# Example Usage:
control_points = [(0, 0), (2, 5), (5, 2), (7, 7)]
draw_bezier_curve_animation(control_points)
