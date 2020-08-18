'''
                                            --- Bubble Sort ---
    Iterate across the array checking if the next index is larger than the previous index. If so swap them.
    Iterative swapping technique to establish sorted order.
    Time Complexity - O(n), Space Complexity - O(1)
'''

import time

def bubble_sort(data, draw_data, time_speed):
    for i in range(len(data) - 1):
        for j in range(len(data) - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                draw_data(data, ['red' if i == j or i == j + 1 else 'blue' for i in range(len(data))])
                time.sleep(time_speed)
    return draw_data(data, ['purple' for i in range(len(data))])
