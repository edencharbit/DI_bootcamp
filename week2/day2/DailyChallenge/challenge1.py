def mat_str_to_mat(matrix_str):
    """Step 1: Transforming the String into a 2D List"""
    matrix = []
    for line in matrix_str.strip().split('\n'):
        row = []
        for char in line:
            row.append(char)
        matrix.append(row)
    return matrix


def matrix_to_str(matrix):
    """Step 2: Processing Columns"""
    mat_to_str = ""
    for i in range(len(matrix[0])):
        for row in matrix:
            mat_to_str += row[i]
    return mat_to_str


def filter_alpha(char):
    """Step 3: Filtering Alpha Characters"""
    return char.isalpha()


def str_symb_free(str_to_filter):
    """Step 4: Replace symbols with spaces"""
    decoded_message = ""
    for char in str_to_filter:
        if filter_alpha(char):
            decoded_message += char
        else:
            decoded_message += " "
    return decoded_message


def decoder(matrix_str):
    """Step 5: Print the decoded message"""
    matrix = mat_str_to_mat(matrix_str)
    mat_to_str = matrix_to_str(matrix)
    decoded_message = str_symb_free(mat_to_str)
    print(decoded_message)


matrix_string = '''
7ir
Tsi
h%x
i ?
sM# 
$a 
#t%'''


decoder(matrix_string)
