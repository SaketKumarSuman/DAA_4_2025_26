import tkinter as tk
import random

root = tk.Tk()
root.title("Sorting Visualizer PRO")
root.geometry("1100x650")
root.config(bg="black")

data = []
rectangles = []
texts = []
running = False
speed = 20


canvas = tk.Canvas(root, bg="white")
canvas.pack(fill=tk.BOTH, expand=True, pady=20)


# ----------- CREATE BARS -----------
def create_bars():
    canvas.delete("all")
    rectangles.clear()
    texts.clear()

    if not data:
        return

    h = canvas.winfo_height()
    w = canvas.winfo_width()
    bar_width = w / len(data)
    max_val = max(data)

    for i, val in enumerate(data):
        x0 = i * bar_width
        y0 = h - (val / max_val) * (h - 40)
        x1 = (i + 1) * bar_width
        y1 = h

        rect = canvas.create_rectangle(x0, y0, x1, y1, fill="blue")
        text = canvas.create_text(x0 + bar_width/2, y0 - 10, text=str(val), font=("Arial", 8))

        rectangles.append(rect)
        texts.append(text)


# ----------- UPDATE BARS -----------
def update_bars(colors=None):
    h = canvas.winfo_height()
    max_val = max(data)

    for i, val in enumerate(data):
        x0, _, x1, y1 = canvas.coords(rectangles[i])
        y0 = h - (val / max_val) * (h - 40)

        canvas.coords(rectangles[i], x0, y0, x1, y1)
        canvas.coords(texts[i], x0 + (x1-x0)/2, y0 - 10)
        canvas.itemconfig(texts[i], text=str(val))

        if colors:
            canvas.itemconfig(rectangles[i], fill=colors[i])

    root.update_idletasks()


# ----------- GENERATE -----------
def generate():
    global data, running
    running = False
    data = [random.randint(10, 100) for _ in range(40)]
    root.after(100, create_bars)


# ----------- STOP -----------
def stop():
    global running
    running = False


# ----------- BUBBLE SORT -----------
def bubble_sort():
    global running
    running = True
    i = j = 0

    def step():
        nonlocal i, j
        if not running:
            return

        if i < len(data):
            if j < len(data) - i - 1:
                colors = ["blue"] * len(data)
                colors[j], colors[j+1] = "red", "red"

                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]

                update_bars(colors)
                j += 1
                root.after(speed, step)
            else:
                j = 0
                i += 1
                root.after(speed, step)
        else:
            update_bars(["green"] * len(data))

    step()


# ----------- SELECTION SORT -----------
def selection_sort():
    global running
    running = True
    i, j, min_idx = 0, 0, 0

    def step():
        nonlocal i, j, min_idx
        if not running:
            return

        if i < len(data):
            if j == 0:
                min_idx = i
                j = i + 1

            if j < len(data):
                if data[j] < data[min_idx]:
                    min_idx = j

                colors = ["blue"] * len(data)
                colors[min_idx], colors[j] = "yellow", "red"

                update_bars(colors)
                j += 1
                root.after(speed, step)
            else:
                data[i], data[min_idx] = data[min_idx], data[i]
                j = 0
                i += 1
                root.after(speed, step)
        else:
            update_bars(["green"] * len(data))

    step()


# ----------- INSERTION SORT -----------
def insertion_sort():
    global running
    running = True
    i = 1

    def step():
        nonlocal i
        if not running:
            return

        if i < len(data):
            j = i
            while j > 0 and data[j] < data[j-1]:
                data[j], data[j-1] = data[j-1], data[j]
                j -= 1
                update_bars(["red" if x == j else "blue" for x in range(len(data))])
            i += 1
            root.after(speed, step)
        else:
            update_bars(["green"] * len(data))

    step()


# ----------- QUICK SORT -----------
def quick_sort():
    global running
    running = True

    def partition(low, high):
        pivot = data[high]
        i = low - 1
        for j in range(low, high):
            if not running:
                return low
            if data[j] < pivot:
                i += 1
                data[i], data[j] = data[j], data[i]
            update_bars(["red" if x == j else "blue" for x in range(len(data))])
        data[i+1], data[high] = data[high], data[i+1]
        return i+1

    def quick(l, r):
        if l < r and running:
            pi = partition(l, r)
            root.after(speed, lambda: quick(l, pi-1))
            root.after(speed, lambda: quick(pi+1, r))

    quick(0, len(data)-1)
    update_bars(["green"] * len(data))


# ----------- MERGE SORT -----------
def merge_sort():
    global running
    running = True

    def merge(l, m, r):
        left = data[l:m+1]
        right = data[m+1:r+1]
        i = j = 0
        k = l

        while i < len(left) and j < len(right):
            if not running:
                return
            if left[i] <= right[j]:
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1
            update_bars(["yellow" if x >= l and x <= r else "blue" for x in range(len(data))])

        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1

    def merge_rec(l, r):
        if l < r and running:
            m = (l + r) // 2
            merge_rec(l, m)
            merge_rec(m+1, r)
            merge(l, m, r)

    merge_rec(0, len(data)-1)
    update_bars(["green"] * len(data))


# ----------- SPEED -----------
def set_speed(val):
    global speed
    speed = val


# ----------- UI -----------
frame = tk.Frame(root, bg="black")
frame.pack()

buttons = [
    ("Generate", generate, "orange"),
    ("Bubble", bubble_sort, "lightgreen"),
    ("Selection", selection_sort, "lightblue"),
    ("Insertion", insertion_sort, "pink"),
    ("Quick", quick_sort, "cyan"),
    ("Merge", merge_sort, "violet"),
    ("STOP", stop, "red")
]

for i, (text, cmd, color) in enumerate(buttons):
    tk.Button(frame, text=text, command=cmd, bg=color).grid(row=0, column=i, padx=5)

tk.Button(frame, text="1x", command=lambda: set_speed(40)).grid(row=1, column=2)
tk.Button(frame, text="2x", command=lambda: set_speed(20)).grid(row=1, column=3)
tk.Button(frame, text="3x", command=lambda: set_speed(5)).grid(row=1, column=4)


# ----------- RESIZE HANDLING -----------
def on_resize(event):
    create_bars()

root.bind("<Configure>", on_resize)


generate()
root.mainloop()