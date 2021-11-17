def averages_list(list_of_values):
    average = sum(list_of_values) / len(list_of_values)
    return list(map(lambda x: x / average, list_of_values))
