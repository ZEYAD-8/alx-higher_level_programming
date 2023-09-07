#!/usr/bin/python3
"""
    2-matrix_divided Module
"""


def matrix_divided(matrix, div):
    """ 
    Divide all elements of a matrix by a specified divisor. 
 
    Args: 
    matrix (list of lists): The input matrix. 
    divisor (int or float): The number by which to divide all elements of the matrix. 
 
    Returns: 
    list of lists: A new matrix with all elements divided by the specified divisor. 
    """ 
    if not type(div) in (int, float):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    if (not isinstance(matrix, list) or matrix == []
        or not all(isinstance(row, list) for row in matrix)
        or has_empty_lists(matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    try:
        uni_len = len(matrix[0])
    except:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    new_matrix = []
    for row in matrix:
        if len(row) != uni_len:
            raise TypeError("Each row of the matrix must have the same size")

        new_row = []
        for element in row:
            if not type(element) in (int, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

            new_row.append(round(element/div, 2))

        new_matrix.append(new_row)


    return new_matrix


def has_empty_lists(matrix):
    """
    Check if a matrix contains any empty lists.

    Args:
    matrix (list of lists): The input matrix.

    Returns:
    bool: True if the matrix contains at least one empty list, False otherwise.
    """
    return any(not row for row in matrix)
