'''
                                            --- Quick Sort ---
    Using a pivot point, usually taking the middle value of the array and setting it to the end.
    Then check if values from left are smaller than pivot and values from right are larger than pivot.
    Swap values, keeping smaller to the left and larger to the right, returning the pivot to its original position.
    Recursively call this swap on left and right sides (partitions) until all values are sorted.
    Time Complexity - O(n logn(n)), Space Complexity - O(log(n))
'''

import time

def quick_sort(data, head, tail, draw_data, time_speed):
    if head < tail:
        partition_idx = partition(data, head, tail, draw_data, time_speed)
        #left partition, -1 / up to but not including partition value
        quick_sort(data, head, partition_idx - 1, draw_data, time_speed)
        #right partition, +1 / above and not including partition value
        quick_sort(data, partition_idx + 1, tail, draw_data, time_speed)
    # return data


def partition(data, head, tail, draw_data, time_speed):
    # to sort each partition, returns index of border (middle value)
    border = head   # start
    pivot = data[tail]  # end
    # visualise data
    draw_data(data, get_colours(data, head, tail, border, border))
    time.sleep(time_speed)

    for i in range(head, tail):
        if data[i] < pivot:
            # visualise during sorting method to see what two elements are swapping
            draw_data(data, get_colours(data, head, tail, border, i, True))
            time.sleep(time_speed)
            # if data from left is smaller than pivot data
            # swap current data with border data and increase the index
            data[border], data[i] = data[i], data[border]
            border += 1

        # visualise at end of each iteration
        draw_data(data, get_colours(data, head, tail, border, i))
        time.sleep(time_speed)
    # finally swap pivot and border returning pivot to its original position, with visualisation
    draw_data(data, get_colours(data, head, tail, border, tail, True))
    time.sleep(time_speed)
    data[border], data[tail] = data[tail], data[border]
    return border


def get_colours(data, head, tail, border, curr_idx, is_swapping = False):
    colour_array = []
    for i in range(len(data)):
        if i >= head and i <= tail:
            colour_array.append('white')
        else:
            colour_array.append('pink')

        if i == tail:
            colour_array[i] = 'yellow'
        elif i == border:
            colour_array[i] = 'blue'
        elif i == curr_idx:
            colour_array[i] = 'red'

        if is_swapping:
            if i == border or i == curr_idx:
                colour_array[i] = 'lime'
    return colour_array
