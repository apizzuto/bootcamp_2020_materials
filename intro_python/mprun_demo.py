
import numpy as np

list_1 = list(np.random.uniform(1, 1000, size=500))

def get_n_smallest(list_, n):
    return sorted(list_)[0:n]

def get_sum(list_):
    sum = 0
    for element in list_:
        sum += element
    return sum

def function(list_):
    output_list = []

    for n, element in enumerate(list_):
        smallest_n = get_n_smallest(list_, n)
        sum_smallest_n = get_sum(smallest_n)
        output_list.append(sum_smallest_n)
