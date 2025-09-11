def is_matrix(item):

    if not isinstance(item, list):
        return False

    if not item:  
        return True 

    row_length = None
    for row in item:
        if not isinstance(row, list):
            return False
        if row_length is None:
            row_length = len(row)
        elif len(row) != row_length:
            return False
        

    return True

def check_list_for_matrices(data_list):
    results = []
    for item in data_list:
        results.append(is_matrix(item))
    return results


list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  
list2 = [[1, 2], [3, 4, 5]]              
list3 = [[1, 'a'], [3, 4]]              
list4 = [1, 2, 3]                        
list5 = []                               
list6 = [[], []]                         
list7 = [[1], [2], [3]]                 
list8 = [[1, 2], [3, [4, 5]]]            
list9 = [[1, 2, None]]                 
my_data_list = [list1, list2, list3, list4, list5, list6, list7, list8, list9, "hello", 123]

matrix_checks = check_list_for_matrices(my_data_list)

for i, is_mat in enumerate(matrix_checks):
    print(f"Item {i+1}: {my_data_list[i]} is a matrix: {is_mat}")
