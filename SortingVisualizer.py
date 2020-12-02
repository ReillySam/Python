'''
                                        --- SORTING VISUALIZER ---
    Developer a sorting visualizer with at least 2 sorting technique e.g. Quick Sort, Merge, Bubble, Insertion.
    Use the separation of concerns design patter for sorting methods.
    Implement using Tkinter to develop a GUI and/or visual interface.
    
    Implement full version using Django. An over all webpage for my CV (December 2020)
'''

from tkinter import *
from tkinter import ttk
import random
from BubbleSort import bubble_sort
from MergeSort import merge_sort
from QuickSort import quick_sort


root = Tk()
root.title("Sorting Algorithm Visualizer")
root.maxsize(900, 600)
root.config(bg="black")


# Variables
selected_algo = StringVar()
data = []


def draw_data(data, colours):
    canvas.delete('all')  # clear data field
    canvas_height = 380
    canvas_width = 600
    x_width = canvas_width / (len(data) + 1)   # bar width
    offset = 30
    spacing = 10
    normalized_data = [i / max(data) for i in data]  # normalize data bars based on the max data
    for i, height in enumerate(normalized_data):
        # top left
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 340
        # bottom right
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colours[i])
        canvas.create_text(x0 + 2, y0, anchor=SW, text=str(data[i]))
    root.update_idletasks()  # update each time an event occurs/data changes


def generate():
    global data

    min_value = int(min_entry.get())
    max_value = int(max_entry.get())
    size = int(size_entry.get())

    data = []
    for _ in range(size):
        data.append(random.randrange(min_value, max_value + 1))

    draw_data(data, ['yellow' for i in range(len(data))])

    
def start_algo():
    global data
    if not data: return
    if algo_menu.get() == 'Quick Sort':
        quick_sort(data, 0, len(data) - 1, draw_data, speed_scale.get())
    elif algo_menu.get() == 'Bubble Sort':
        bubble_sort(data, draw_data, speed_scale.get())
    elif algo_menu.get() == 'Merge Sort':
        merge_sort(data, draw_data, speed_scale.get())

    draw_data(data, ['purple' for i in range(len(data))])


# Frame and base layout
UI_frame = Frame(root, width=620, height=200, bg='gray')
UI_frame.grid(row=0, column=0, padx=10, pady=10)

canvas = Canvas(root, width=620, height=380, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=10)

# User interface area
# Row 0
Label(UI_frame, text='Algorithm', bg='gray').grid(row=0, column=0, padx=5, pady=5, sticky=W)

# Dropdown box choice
algo_menu = ttk.Combobox(UI_frame, textvariable=selected_algo, values=['Bubble Sort', 'Merge Sort', 'Quick Sort'])
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)

# Speed Scale
speed_scale = Scale(UI_frame, from_=0.1, to=1.0, length=200, digits=2, resolution=0.1, orient=HORIZONTAL, label='Select Speed [s]')
speed_scale.grid(row=0, column=2, padx=5, pady=5)

# Start button
Button(UI_frame, text='Start', command=start_algo, bg='lime').grid(row=0, column=3, padx=5, pady=5)

# Row 1 Entries
size_entry = Scale(UI_frame, from_=3, to=30, length=150, resolution=2, orient=HORIZONTAL, label='Data Size')
size_entry.grid(row=1,  column=0, padx=5, pady=5)

min_entry = Scale(UI_frame, from_=1, to=10, length=150, resolution=1, orient=HORIZONTAL, label='Min Value')
min_entry.grid(row=1,  column=1, padx=5, pady=5)

max_entry = Scale(UI_frame, from_=10, to=100, length=150, resolution=5, orient=HORIZONTAL, label='Max Value')
max_entry.grid(row=1,  column=2, padx=5, pady=5)

# Generate button
Button(UI_frame, text='Generate', command=generate, bg='white').grid(row=1, column=3, padx=5, pady=5)

# call root and UI frame main
root.mainloop()
