import colorsys
import random
from pyray import * #type:ignore

# colored sorting algorithm visualizer
# by las-r

# settings
AMNT = 500
OPF = 100

# init
init_window(AMNT, AMNT, "Color Sorting Alg Visualizer")

# helpers
def ntocol(n, mn=AMNT-1):
    hue = max(0, min(1, n / mn))
    hue *= 0.8
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
    return (round(r * 255), round(g * 255), round(b * 255), 255)
    
def swap(i, j):
    l[i], l[j] = l[j], l[i]
    
# sort
def sort():
    n = len(l)
    while True:
        nn = 0
        for i in range(1, n):
            if l[i - 1] > l[i]:
                l[i - 1], l[i] = l[i], l[i - 1]
                nn = i
                yield
        n = nn
        if n <= 1:
            break

# variables
t = 0
l = [i for i in range(0, AMNT)]
sorting = False
sorter = None
random.shuffle(l)

# main loop
while not window_should_close():
    if is_key_pressed(KeyboardKey.KEY_R):
        t = 0
        sorting = False
        sorter = None
        random.shuffle(l)
    if is_key_pressed(KeyboardKey.KEY_SPACE):
        sorting = not sorting
        if sorting and sorter is None:
            sorter = sort()
        
    if sorting and sorter is not None:
        try:
            for _ in range(OPF):
                next(sorter)
                t += 1
        except StopIteration:
            sorting = False
            sorter = None
        
    begin_drawing()
    clear_background(BLACK)
    for i, v in enumerate(l):
        draw_rectangle(i, AMNT - v, 1, v, ntocol(v))
    draw_text(f"t: {t}", 2, 2, 10, WHITE)
    end_drawing()

# deinit
close_window()
