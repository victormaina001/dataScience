
# returns an array of all possible 2 X 2 combinations
def subdivide_matrix(two_dimensional_matrix):
    matrix_height = len(two_dimensional_matrix) - 1
    matrix_width = len(two_dimensional_matrix[0]) - 1
    sub_matrices = []

    for row in range(matrix_width):
        for col in range(matrix_height):
            first_row = [two_dimensional_matrix[row][col], two_dimensional_matrix[row][col + 1]]
            second_row = [two_dimensional_matrix[row + 1][col], two_dimensional_matrix[row + 1][col + 1]]
            sub_matrices.append([first_row, second_row])
    
    return sub_matrices


# finds largest value in each submatrix. Returns an array of arrays with only one element
def find_largest_submatrix_value(three_D_array):
    output = []

    for two_D_array_index in range(len(three_D_array)):
        largest_value_in_two_D_array = [0]

        for array in three_D_array[two_D_array_index]:
            array.sort()
            largest_value_in_array = int(array[-1])
            if largest_value_in_array > largest_value_in_two_D_array[0]:
                largest_value_in_two_D_array[0] = largest_value_in_array
        output.append(largest_value_in_two_D_array)
    
    return output

# finds smallest value in each submatrix. Returns an array of arrays with only one element
def find_smallest_submatrix_value(three_D_array):
    output = []

    for two_D_array_index in range(len(three_D_array)):
        smallest_value_in_two_D_array = three_D_array[two_D_array_index][0]
        for array in three_D_array[two_D_array_index]:
            array.sort()
            smallest_value_in_array = int(array[0])
            if smallest_value_in_array < smallest_value_in_two_D_array[0]:
                smallest_value_in_two_D_array[0] = smallest_value_in_array
        output.append([smallest_value_in_two_D_array[0]])
    
    return output


matrix = [[1, 5, 7], [7, 3, 5], [2, 6, 9]]
submatrices = subdivide_matrix(matrix)

print(subdivide_matrix(matrix))
print(find_largest_submatrix_value(submatrices))
print(find_smallest_submatrix_value(submatrices))