def multiply_list_by_average(list_of_values):
    average = sum(list_of_values) / len(list_of_values)
    return map(lambda x: x * average, list_of_values)
