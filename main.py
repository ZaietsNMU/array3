import importlib

import TK_1
import TK_2
import TK_3
import TK_4

if __name__ == '__main__':
    input_lst = TK_1.input_list(5)
    min_max = TK_2.min_and_max(input_lst)
    avg_list = TK_3.averages_list(input_lst)
    multiply_list = TK_4.multiply_list_by_average(input_lst)
    module = importlib.import_module("TK_5")
    quad = module.quad_list(input_lst)
    print("input list: " + str(input_lst))
    print("min_and_max: " + str(TK_2.min_and_max(input_lst)))
    print("averages_list: " + str(TK_3.averages_list(input_lst)))
    print("ultiply_list_by_average: " + str(TK_4.multiply_list_by_average(input_lst)))
    print("quad_list: " + str(module.quad_list(input_lst)))

