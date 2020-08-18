'''
                                            --- Merge Sort ---
    Recursively split the array into single elements. Reconstruct array by building the array from its single
    elements, comparing their size, fitting them in sorted order. Merge each segment in sorted order until the
    entire array has been sorted to it original length.
    Divide and conquer technique.
    Time Complexity - O(n log(n)), Space Complexity - O(n)
'''

import time


def merge_sort(data, draw_data, time_speed):
    merge_sort_alg(data, 0, len(data) - 1, draw_data, time_speed)


def merge_sort_alg(data, left, right, draw_data, time_speed):
    if left < right:
        # split array recursively
        middle = (left + right) // 2
        merge_sort_alg(data, left, middle, draw_data, time_speed)
        merge_sort_alg(data, middle + 1, right, draw_data, time_speed)
        # merge lists back together in sorted order
        merge(data, left, middle, right, draw_data, time_speed)


def merge(data, left, middle, right, draw_data, time_speed):
    # visualisation before iteration
    draw_data(data, get_colours(data, left, middle, right))
    time.sleep(time_speed)

    left_part = data[left:middle + 1]
    right_part = data[middle + 1: right + 1]

    left_idx = right_idx = 0

    for data_idx in range(left, right + 1):
        if left_idx < len(left_part) and right_idx < len(right_part):
            if left_part[left_idx] <= right_part[right_idx]:
                data[data_idx] = left_part[left_idx]
                left_idx += 1
            else:
                data[data_idx] = right_part[right_idx]
                right_idx += 1
        # if left or right lists contain remaining values, add them
        elif left_idx < len(left_part):
            data[data_idx] = left_part[left_idx]
            left_idx += 1
        else:
            data[data_idx] = right_part[right_idx]
            right_idx += 1

    draw_data(data, ["green" if i >= left and i <= right else "pink" for i in range(len(data))])
    time.sleep(time_speed)


def get_colours(data, left, middle, right):
    colour_array = []

    for i in range(len(data)):
        # larger sublist
        if i >= left and i <= right:
            # inner sublist
            if i >= left and i <= middle:
                colour_array.append("red")
            else:
                colour_array.append("blue")
        # outer sublist
        else:
            colour_array.append("pink")
    return colour_array
